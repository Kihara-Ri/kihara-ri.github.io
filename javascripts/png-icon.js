// 引用 jpg 格式图标

document.addEventListener("DOMContentLoaded", function() {
  //获取文档中所有包含特定文本的元素
  var elements = document.querySelectorAll(":mc-grass-block:")
  // 遍历这些元素
  elements.forEach(function(el) {
    var img = document.createElement("img");
    img.src = "../overrides/.icons/mc/grass-block.png";
    img.alt = "grass-block";
    img.style.width = "24px";
    img.style.height = "24px";
    //替换元素内容
    el.parentNode.replaceChild(img, el)
  });
})