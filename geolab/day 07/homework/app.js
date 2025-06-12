var email = document.getElementById('floatingInput')
var pass = document.getElementById('floatingPassword')
var username= document.getElementById('floatingUname')
var checkbox = document.getElementById('gridCheck')
var button = document.getElementById('button')
var cardtxt = document.getElementById('cardtxt')
var cardtitle = document.getElementById('cardtitle')


button.onclick=() => {
    // console.log(email.value)
    // console.log(pass.value)
    // console.log(username.value)
    // console.log(checkbox.value)

    cardtitle.textContent = username.value
    cardtxt.textContent = 'Mail: ' + email.value
    document.location = 'profile.html'
    
}