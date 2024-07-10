/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


$(document).ready(function () {
    // Function to update quantity input value
    function updateQuantity(productId, newValue) {
        $('#quantity-' + productId).val(newValue);
    }
$('.increment').click(function () {
        var productId = $(this).attr('data-product-id');
        var quantityInput = $('#quantity-' + productId);
        var currentValue = parseInt(quantityInput.val());
        var newValue = currentValue + 1;
        quantityInput.val(newValue);
        updateQuantity(productId, newValue); // Update displayed quantity
    });

    // Decrement button click handler
    $('.decrement').click(function () {
        var productId = $(this).attr('data-product-id');
        var quantityInput = $('#quantity-' + productId);
        var currentValue = parseInt(quantityInput.val());
        if (currentValue > 1) {
            var newValue = currentValue - 1;
            quantityInput.val(newValue);
            updateQuantity(productId, newValue); // Update displayed quantity
        }
    });
   
});

