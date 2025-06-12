const btn = document.getElementById('MYbtn')
const unameid = document.getElementById('MYunameid')

btn.addEventListener('click',()=>{
    document.location = "/profile/"+unameid.value
})
