// 监听文档加载完成事件
document.addEventListener('DOMContentLoaded', function () {
    // 定义调整侧边栏位置的函数
    function adjustSidebar() {
        var sidebar = document.getElementById('sidebar'); // 获取侧边栏元素
        var mainContent = document.getElementById('main'); // 获取主内容区元素
        var headerHeight = document.querySelector('.head').offsetHeight; // 获取头部元素的高度

        // 获取主内容区和侧边栏相对于视口的位置信息
        var mainRect = mainContent.getBoundingClientRect();
        var sidebarRect = sidebar.getBoundingClientRect();

        // 确定侧边栏在视口中的最大和最小Y坐标位置
        var maxSidebarTop = window.innerHeight - sidebarRect.height; // 侧边栏的最大顶部位置
        var minSidebarTop = headerHeight; // 侧边栏的最小顶部位置

        // 当主内容区的顶部在视口内，并且低于头部高度时
        if (mainRect.top > 0 && mainRect.top <= minSidebarTop) {
            sidebar.style.position = 'fixed'; // 固定侧边栏位置
            // 设置侧边栏顶部位置，确保它不超出最大和最小Y坐标范围
            sidebar.style.top = Math.min(maxSidebarTop, Math.max(minSidebarTop, mainRect.top)) - 20 + 'px';
        }

        // 当主内容区的顶部在视口之上时
        else if (mainRect.top <= 0) {
            sidebar.style.position = 'fixed'; // 固定侧边栏位置
            // 设置侧边栏顶部位置，确保它不超出最大Y坐标范围
            sidebar.style.top = Math.min(maxSidebarTop, minSidebarTop) - 65 + 'px';
        } else {
            // 当主内容区的顶部在视口之下时
            sidebar.style.position = 'absolute'; // 使用绝对定位
            // 设置侧边栏顶部位置与主内容区的顶部对齐
            sidebar.style.top = mainContent.offsetTop - 20 + 'px';
        }
    }

    // 添加滚动事件监听器，每次滚动时调整侧边栏位置
    window.addEventListener('scroll', adjustSidebar);
    // 页面加载时也调整一次侧边栏位置
    window.onload = adjustSidebar;
});
