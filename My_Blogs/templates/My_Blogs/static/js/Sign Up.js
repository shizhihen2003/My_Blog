// 监听文档加载完成事件，以确保在DOM元素加载后执行脚本
document.addEventListener('DOMContentLoaded', function () {
    // 获取表单相关的输入字段和按钮
    const usernameInput = document.getElementById('username'); // 获取用户名输入框
    const passwordInput = document.getElementById('password'); // 获取密码输入框
    const passwordConfirmationInput = document.getElementById('password_confirmation'); // 获取密码确认输入框
    const signUpButton = document.querySelector('form button'); // 获取表单内的提交按钮
    const form = document.getElementById('signupForm'); // 获取注册表单元素

    // 给各个输入框添加聚焦和失焦事件监听器，用于显示和隐藏提示信息
    addFocusListeners(usernameInput, 'usernameTip'); // 为用户名输入框添加监听器
    addFocusListeners(passwordInput, 'passwordTip'); // 为密码输入框添加监听器
    addFocusListeners(passwordConfirmationInput, 'passwordConfirmationTip'); // 为密码确认输入框添加监听器

    // 给注册按钮添加点击事件监听器
    signUpButton.addEventListener('click', function (e) {
        e.preventDefault(); // 阻止按钮的默认提交行为
        let hasError = false; // 用于记录表单是否有验证错误的标志

        // 验证用户名是否符合规则
        if (!validateUsername(usernameInput.value)) {
            showError('usernameTip'); // 如果不符合，则显示用户名错误提示
            hasError = true; // 更新错误标志
        }

        // 验证密码是否符合规则
        if (!validatePassword(passwordInput.value)) {
            showError('passwordTip'); // 如果不符合，则显示密码错误提示
            hasError = true; // 更新错误标志
        }

        // 验证两次输入的密码是否一致
        if (passwordInput.value !== passwordConfirmationInput.value) {
            showError('passwordConfirmationTip'); // 如果不一致，则显示密码确认错误提示
            hasError = true; // 更新错误标志
        }

        // 如果没有验证错误，则提交表单
        if (!hasError) {
            form.submit(); // 提交表单
        }
    });
});

// 定义一个函数，用于给输入框添加聚焦和失焦事件的监听器
function addFocusListeners(inputElement, tipElementId) {
    // 当输入框获得焦点时执行
    inputElement.addEventListener('focus', function () {
        // 获取提示元素并使其可见
        document.getElementById(tipElementId).classList.add('visible');
    });
    // 当输入框失去焦点时执行
    inputElement.addEventListener('blur', function () {
        // 获取提示元素并使其不可见
        document.getElementById(tipElementId).classList.remove('visible');
    });
}

// 定义一个函数，用于验证用户名的有效性
function validateUsername(username) {
    // 定义一个正则表达式，用于匹配有效的用户名
    const usernameRegex = /^[a-zA-Z0-9@\.\+\-\/_]{1,150}$/;
    // 测试用户名是否符合正则表达式的规则
    return usernameRegex.test(username);
}

// 定义一个函数，用于验证密码的有效性
function validatePassword(password) {
    // 检查密码长度是否小于8，或者是否全为数字，或者是否为'12345678'
    if (password.length < 8 || /^\d+$/.test(password) || password === '12345678') {
        return false; // 如果以上条件满足任何一条，返回false
    }
    return true; // 否则返回true
}

// 定义一个函数，用于显示错误提示
function showError(tipElementId) {
    // 获取指定的提示元素
    const tipElement = document.getElementById(tipElementId);
    tipElement.classList.add('visible'); // 使提示元素可见
    // 设置5秒后自动隐藏提示
    setTimeout(() => {
        tipElement.classList.remove('visible'); // 使提示元素不可见
    }, 5000);
}
