// 监听文档加载完成事件，确保在整个HTML文档被完全加载和解析后执行脚本
document.addEventListener('DOMContentLoaded', function () {
    // 获取背景模糊相关的DOM元素
    var filterElement = document.getElementById('filter'); // 获取用于实现背景模糊效果的元素
    var toggleButton = document.getElementById('toggleBlur'); // 获取用于切换背景模糊效果的按钮

    // 给切换按钮添加点击事件监听器
    toggleButton.addEventListener('click', function () {
        // 当点击按钮时，切换'filterElement'元素的'class'，添加或移除'blurred'类
        // 'classList.toggle'方法会检查元素是否已包含该类，
        // 如果有，则移除它，如果没有，则添加它
        filterElement.classList.toggle('blurred');
    });
});
