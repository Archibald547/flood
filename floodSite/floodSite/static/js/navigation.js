var clickDropdownObjects;
var currentDropped = null;
var dropDownLock = false;
var usernameArea;

$(document).ready(function(){

    clickDropdownObjects = $("[data-dropdown=\"click\"]");
    clickDropdownObjects.click(clickItem);

    $("body").click(onClick);
});

function showDropdown(dropdown, lock){
    if(currentDropped != null){
        currentDropped.stop(true);
        currentDropped.fadeOut(0);
        dropdown.fadeIn(0);
    }
    else{
        dropdown.fadeIn(DROPDOWN_FADE_DELAY);
    }
    currentDropped = dropdown;
    dropDownLock = lock;
}
