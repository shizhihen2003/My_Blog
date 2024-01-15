// 添加事件监听器，在整个HTML文档被完全加载和解析完成后立即执行
document.addEventListener('DOMContentLoaded', function () {

    // --- 标题栏高亮功能 ---
    // 获取当前页面的标题
    var pageTitle = document.title;
    // 选择所有在'.pages a'选择器下的链接元素
    var links = document.querySelectorAll('.pages a');
    // 对每个链接执行以下操作
    links.forEach(function (link) {
        // 如果链接的文本内容包含在页面标题中
        if (pageTitle.includes(link.textContent.trim())) {
            // 为该链接添加'active-link'类，通常用于高亮显示当前页面的链接
            link.classList.add('active-link');
        }
    });

    // --- 搜索功能的实现 ---
    // 选择类名为'right'的元素下的第一个<a>元素，通常是触发搜索的链接或按钮
    var searchLink = document.querySelector('.right a');
    // 通过ID获取模态背景、搜索模态框、关闭按钮、搜索按钮和搜索输入框的DOM元素
    var modalBackground = document.getElementById('modalBackground');
    var searchModal = document.getElementById('searchModal');
    var closeModal = document.getElementById('closeModal');
    var searchButton = document.getElementById('searchButton');
    var searchInput = document.getElementById('searchInput');

    // 当点击搜索链接时执行以下操作
    searchLink.addEventListener('click', function (e) {
        e.preventDefault(); // 阻止链接的默认动作，即不让页面跳转
        modalBackground.classList.add('show'); // 为模态背景添加'show'类来显示它
        searchModal.classList.add('show'); // 为搜索模态框添加'show'类来显示它
        closeModal.classList.remove('hidden'); // 移除关闭按钮的'hidden'类来显示它
        searchInput.focus(); // 将焦点设置到搜索输入框，方便用户立即输入
    });

    // 当点击关闭按钮时执行以下操作
    closeModal.addEventListener('click', function () {
        modalBackground.classList.remove('show'); // 移除模态背景的'show'类来隐藏它
        searchModal.classList.remove('show'); // 移除搜索模态框的'show'类来隐藏它
        this.classList.add('hidden'); // 为关闭按钮添加'hidden'类来隐藏它
    });

    // 当点击搜索按钮时执行以下操作
    searchButton.addEventListener('click', function () {
        var searchTerm = searchInput.value.trim(); // 获取搜索输入框的值并去除前后空格
        // 如果输入框中有值（即用户输入了搜索词）
        if (searchTerm) {
            console.log('Searching for:', searchTerm); // 在控制台打印搜索词
            // 此处可以添加实际的搜索逻辑，如发送请求到服务器或过滤当前页面内容
        }
    });

});
