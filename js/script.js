var category = document.getElementsByClassName("list-categories");
var k;
for (k = 0; k < category.length; k++) {
  category[k].addEventListener("click", function() {
    this.classList.toggle("active");
    var categoryList = this.nextElementSibling;
    if (categoryList.style.display === "block") {
      categoryList.style.display = "none";
    } else {
      categoryList.style.display = "block";
    }
  });
}

var images = document.getElementsByClassName("product-img");
for (var i = 0; i < images.length; i++) {
  images[i].onclick = function() {
    document.querySelector(".modal").style.display = "flex";
  };
}

document.querySelector(".close").addEventListener("click", function() {
  document.querySelector(".modal").style.display = "none";
});
/**var delete_item = document.getElementsByClassName("btn-delete");

for (var l = 0; l < delete_item; l++) {
  delete_item[l].onclick = deleteVal();
}

function deleteVal() {
  document.querySelector(".modal").style.display = "none";
  this.parentElement.style.display = "none";
}

document.getElementById("add-product").addEventListener("click", function() {
  document.querySelector(".modal2").style.display = "flex";
}); */
