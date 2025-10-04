import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
from lightgbm import LGBMRegressor
from sklearn.metrics import accuracy_score
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
test_ids = test["Id"]
y = train["SalePrice"]
train.drop(["SalePrice"], axis=1, inplace=True)
all_data = pd.concat([train, test], sort=False).reset_index(drop=True)
all_data.drop("Id", axis=1, inplace=True)
for col in ["Alley","PoolQC","Fence","MiscFeature","FireplaceQu",
            "GarageType","GarageFinish","GarageQual","GarageCond",
            "BsmtQual","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinType2",
            "MasVnrType"]:
    all_data[col] = all_data[col].fillna("None")
for col in ["GarageYrBlt","GarageArea","GarageCars",
            "BsmtFinSF1","BsmtFinSF2","BsmtUnfSF","TotalBsmtSF",
            "BsmtFullBath","BsmtHalfBath","MasVnrArea"]:
    all_data[col] = all_data[col].fillna(0)
all_data["LotFrontage"] = all_data.groupby("Neighborhood")["LotFrontage"] \
                                  .transform(lambda x: x.fillna(x.median()))
all_data["Electrical"] = all_data["Electrical"].fillna(all_data["Electrical"].mode()[0])
all_data["TotalSF"] = all_data["GrLivArea"] + all_data["TotalBsmtSF"] + all_data["GarageArea"]
all_data["HasGarage"] = (all_data["GarageArea"] > 0).astype(int)
all_data["HasPool"] = (all_data["PoolArea"] > 0).astype(int)
all_data["HasFireplace"] = (all_data["Fireplaces"] > 0).astype(int)
qual_map = {"Ex":5,"Gd":4,"TA":3,"Fa":2,"Po":1}
for col in ["ExterQual","ExterCond","BsmtQual","BsmtCond","HeatingQC","KitchenQual",
            "FireplaceQu","GarageQual","GarageCond"]:
    all_data[col] = all_data[col].map(qual_map).fillna(0)
all_data = pd.get_dummies(all_data)
n_train = train.shape[0]
X = all_data.iloc[:n_train, :]
X_test = all_data.iloc[n_train:, :]
y = np.log1p(y)   
kf = KFold(n_splits=5, shuffle=True, random_state=42)
oof_preds = np.zeros(X.shape[0])
test_preds = np.zeros(X_test.shape[0])
for fold, (tr_idx, val_idx) in enumerate(kf.split(X, y)):
    X_tr, X_val = X.iloc[tr_idx], X.iloc[val_idx]
    y_tr, y_val = y.iloc[tr_idx], y.iloc[val_idx]
    model = LGBMRegressor(
    n_estimators=2000,   
    learning_rate=0.01,
    num_leaves=31,
    colsample_bytree=0.8,
    subsample=0.8,
    random_state=42
)
    model.fit(
        X_tr, y_tr,
        eval_set=[(X_val, y_val)]
    )
    oof_preds[val_idx] = model.predict(X_val)
    test_preds += model.predict(X_test) / kf.n_splits
rmse = np.sqrt(mean_squared_error(y, oof_preds))
print("CV RMSE on log target:", rmse)
final_preds = np.expm1(test_preds)
submission = pd.DataFrame({"Id": test_ids, "SalePrice": final_preds})
submission.to_csv("submission.csv", index=False)
print("submission.csv is ready!")

