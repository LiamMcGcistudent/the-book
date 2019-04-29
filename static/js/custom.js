$(document).ready(function() {
    
    $(".new-input-btn").on("click", function() {
        $('<input type="text" class="form-control ingredient" name="ingredient" id="ingredient"  >').insertBefore(".new-input-btn");
    });
    
    $(".remove-input-btn").on("click", function() {
        $("#ingredients-row input:last").remove();
    });
    
    $(".inst-input-btn").on("click", function() {
        $('<input type="text" class="form-control" name="instructions" id="instructions" >').insertBefore(".inst-input-btn");
    });
    
    $(".inst-remove-input-btn").on("click", function() {
        $("#instructions-row input:last").remove();
    });
    
    $(".cat-input-btn").on("click", function() {
        $('<input type="text" class="form-control" name="category" id="category" >').insertBefore(".cat-input-btn");
    });
    
    $(".cat-remove-input-btn").on("click", function() {
        $("#cat-row input:last").remove();
    });
    
    $(".all-input-btn").on("click", function() {
        $('<input type="text" class="form-control" name="allergen" id="allergen" >').insertBefore(".all-input-btn");
    });
    
    $(".all-remove-input-btn").on("click", function() {
        $("#all-row input:last").remove();
    });
})