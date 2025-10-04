// Simple script to add interactivity

document.addEventListener("DOMContentLoaded", () => {
    const img = document.getElementById("apod-img");

    img.addEventListener("click", () => {
        // Toggle fullscreen view
        if (img.classList.contains("fullscreen")) {
            img.classList.remove("fullscreen");
            document.body.style.overflow = "auto";
        } else {
            img.classList.add("fullscreen");
            document.body.style.overflow = "hidden";
        }
    });
});

// Extra CSS injection for fullscreen mode
const style = document.createElement("style");
style.innerHTML = `
    .fullscreen {
        position: fixed !important;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) scale(1.05) !important;
        max-width: 95vw !important;
        max-height: 95vh !important;
        z-index: 9999 !important;
        border-radius: 10px !important;
        box-shadow: 0 0 25px rgba(255,255,255,0.7);
    }
`;
document.head.appendChild(style);
