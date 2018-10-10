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
document
  .getElementsByClassName("open-details")
  .addEventListener("click", function() {
    document.querySelector(".modal").style.display = "flex";
  });
//Modal Close code...
document.getElementsByClassName("close").addEventListener("click", function() {
  document.querySelector(".modal").style.display = "none";
});
