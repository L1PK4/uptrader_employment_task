document.querySelectorAll(".expand").forEach(item => {
    const div = item
        .nextElementSibling
        .nextElementSibling;
    item.addEventListener('click', e => {
        const closed = div
            .className
            .indexOf("closed");
        if (closed == -1) {
            div.className += "closed";
            item.style.backgroundColor = "red";
        }
        else {
            div.className = div.className.slice(0, closed);
            item.style.backgroundColor = "green";
        }
    })
    const closed = div
            .className
            .indexOf("closed");
    if (closed == -1) {
        item.style.backgroundColor = "green";
    }
    else {
        item.style.backgroundColor = "red";
    }
});