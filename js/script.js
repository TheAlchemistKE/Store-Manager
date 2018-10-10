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

var open_details = document.getElementsByClassName("open-details");
var list;
for (list = 0; list < open_details.length; list++) {
  open_details[list].addEventListener("click", function() {
    document.querySelector(".modal").style.display = "flex";
  });
} 
document.querySelector(".close").addEventListener("click", function() {
  document.querySelector(".modal").style.display = "none";
});
