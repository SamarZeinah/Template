document.addEventListener('DOMContentLoaded', function () {
    var subscribeButton = document.querySelector('.btn');
    var emailInput = document.getElementById('user-text');
    subscribeButton.addEventListener('click', function () {
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (emailRegex.test(emailInput.value)) {
            subscribeButton.style.backgroundColor = 'orange';
          
            window.location.href = 'index.html';
        } else {
            validEmailMessage.style.color = 'red';
            validEmailMessage.innerHTML = 'Not Valid Email';
     }
});
});
