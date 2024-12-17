// 页面加载时获取所有图片
document.addEventListener("DOMContentLoaded", fetchImages);

function fetchImages() {
    const searchQuery = document.getElementById("searchInput").value; // 获取搜索输入框的值
    let url = "/api/images/";

    // 如果有搜索条件，过滤结果
    if (searchQuery) {
        url += `?search=${searchQuery}`;
    }

    // 发起 GET 请求获取图片数据
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const gallery = document.getElementById("imageGallery");
            gallery.innerHTML = ""; // 清空当前内容

            // 遍历 API 返回的数据
            data.forEach(image => {
                const imgElement = document.createElement("img");
                imgElement.src = image.image_file; // 图片路径
                imgElement.alt = image.title; // 图片标题
                imgElement.title = image.title;

                gallery.appendChild(imgElement); // 添加到页面
            });

            if (data.length === 0) {
                gallery.innerHTML = "<p>No images found</p>";
            }
        })
        .catch(error => console.error("Error fetching images:", error));
}
