let highestprice = document.getElementById("highestprice");
let lowestprice = document.getElementById("lowestprice");
let startprice = document.getElementById("startprice");
let tradingvolume = document.getElementById("tradingvolume");
let confirmbtn = document.getElementById("confirm");
let mood = "confirm";

let dataPro;
if (localStorage.product != null) {
  dataPro = JSON.parse(localStorage.product);
} else {
  dataPro = [];
}
//the goal ==>when click on confirm save data in array(dataPro)
confirmbtn.onclick = function () {
  //I have to collect data for one product in Object
  let newPro = {
    highestprice: highestprice.value,
    lowestprice: lowestprice.value,
    startprice: startprice.value,
    tradingvolume: tradingvolume.value,
  };
  //    dataPro.push(newPro)==>this line uesd to creat object
  dataPro.push(newPro);

  //go to local storage add save items that was in array ==>This will make the data available even if you reload
  // JSON.stringify(dataPro)==>local storage take string only
  localStorage.setItem("product", JSON.stringify(dataPro));
  //call function when click on button
  clearData();
  showData();
    
                          // ################

// إرسال البيانات للتنبؤ وعرض النتيجة
fetch("/predict", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    highestprice: highestprice.value,
    lowestprice: lowestprice.value,
    startprice: startprice.value,
    tradingvolume: tradingvolume.value,
  }),
})
.then(response => response.json())
.then(data => {
  // عرض النتيجة على الصفحة
  document.getElementById("predicted_price").innerText = "Predicted Price: " + data.predicted_price;
})
.catch(error => {
  console.error("Error:", error);
});
    
                              // ################

  
};

function clearData() {
  highestprice.value = "";
  lowestprice.value = "";
  startprice.value = "";
  tradingvolume.value = "";
}
//#05-read==>data that was in local storage appear in page when click on button create
function showData() {
  // make empty table and but on it data that was in dataPro(array)using for loop
  let table = "";
  for (let i = 0; i < dataPro.length; i++) {
    table += `
                <tr>
                    <td>${dataPro[i].highestprice}</td>
                    <td>${dataPro[i].lowestprice}</td>
                    <td>${dataPro[i].startprice}</td>
                    <td>${dataPro[i].tradingvolume}</td>
                </tr>
`;
  }
  document.getElementById("tbody").innerHTML = table;
}
start.onclick=function(){
  document.querySelector('.face').remove();
  // console.log(face);
}




















