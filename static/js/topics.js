// 在文档加载完成后执行函数
document.addEventListener('DOMContentLoaded', function () {
    // 选择所有类名为'topic'的元素
    var topics = document.querySelectorAll('.topic');

    // 遍历所有选中的文章元素
    topics.forEach(function (topic) {
        // 为每个文章元素添加鼠标进入事件监听
        topic.addEventListener('mouseenter', function () {
            // 当鼠标进入文章时执行以下操作：
            this.style.transform = 'scale(1.05)'; // 将文章放大到原来的1.05倍
            this.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.4)'; // 增加阴影的模糊度和颜色深度
        });

        // 为每个文章元素添加鼠标离开事件监听
        topic.addEventListener('mouseleave', function () {
            // 当鼠标离开文章时执行以下操作：
            this.style.transform = 'scale(1)'; // 将文章大小恢复到原始尺寸
            this.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.2)'; // 恢复阴影到较轻的状态
        });
    });
});
