// 为清空按钮绑定点击事件
document.getElementById('clearButton').addEventListener('click', function() {
    // 清空输入框
    document.getElementById('search_box').value = '';
});


// 更新搜索模式的函数
function updateSearchMode() {
    const searchMode = document.getElementById('search_mode').value;
    const searchPrompt = document.getElementById('search-prompt');
    const searchInput = document.getElementById('search_box');

    if (searchMode === 'movie') {
        searchPrompt.innerText = '请输入电影名：';
        searchInput.placeholder = '请输入电影名';
    } else {
        searchPrompt.innerText = '请输入视频网址：';
        searchInput.placeholder = '请粘贴视频网址';
    }
}



document.getElementById('sendButton').addEventListener('click', function() {
    // 获取输入框的值
    var search_box = document.getElementById('search_box').value;
    var line = document.getElementById('line').value;

    // 发送 AJAX 请求到后端 Flask
    fetch('/receive', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            line1: line,
            choose_mode: document.getElementById('search_mode').value,
            web1: search_box
        })
    })
    .then(response => response.json())  // 解析响应为 JSON
    .then(data => {
        if (data.status === "success") {
            var generatedLink = data.generated_link;
            window.open(generatedLink, '_blank');  // 打开生成的链接
        } else {
            alert(data.message);  // 如果返回错误消息，显示弹窗
        }
    })
    .catch(error => {
        console.error('请求失败: ' + error);
        alert('请求失败，请检查输入内容');
    });
});



