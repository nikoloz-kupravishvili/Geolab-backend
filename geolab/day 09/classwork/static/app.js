
const btn = document.getElementById('btn')
const unameid = document.getElementById('unameid')

btn.addEventListener('click',()=>{
    document.location = "/profile/"+unameid.value
})

// function domain() {
//     console.log("/"+unameid.value)
// }