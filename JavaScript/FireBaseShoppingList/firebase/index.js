import { add } from "./fun.js"
import {initializeApp} from "https://www.gstatic.com/firebasejs/9.19.1/firebase-app.js"
import {getDatabase,ref,push,onValue,remove} from "https://www.gstatic.com/firebasejs/9.19.1/firebase-database.js"
const appSetting={
    databaseURL:"https://projectbase-a6bdc-default-rtdb.firebaseio.com/"
}
const app =initializeApp(appSetting)
const db=getDatabase(app)
const dbshopinglist=ref(db,"shoppinglist")
console.log(add(5,5))

const inputfieldel=document.getElementById("input_fiels")
const addButtonfield=document.getElementById("add-button")
const shoppinglist=document.getElementById("shopping-list")

addButtonfield.addEventListener("click",function(){
    let inputValue=inputfieldel.value
    push(dbshopinglist,inputValue)
    inputfieldel.value=""
})

onValue(dbshopinglist,function(snapshot){
    if (snapshot.exists()){
        let itemArray=Object.entries(snapshot.val())
        console.log(itemArray)
        shoppinglist.innerHTML=""
        for(let i =0; i<itemArray.length; i++){
            appendtoshoppinglist(itemArray[i])
    }
    }
    else{
        shoppinglist.innerHTML="Nothing in the cart, Please add something"
    }
    }
)

function appendtoshoppinglist(item){
    let itemid=item[0]
    let itemvalur=item[1]
    let newel=document.createElement("li")
    newel.textContent=itemvalur
    newel.addEventListener("click",function(){
        let getlocal=ref(db,`shoppinglist/${itemid}`)
        remove(getlocal)
    })
    shoppinglist.append(newel)

}

