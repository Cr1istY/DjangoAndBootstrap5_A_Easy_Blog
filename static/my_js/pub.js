window.onload= function () {
    const {createEditor, createToolbar} = window.wangEditor

    const editorConfig = {
        placeholder: 'Type here...',
        onChange(editor) {
            const html = editor.getHtml()
            console.log('editor content', html)
            // 也可以同步到 <textarea>
        },
    }

    const editor = createEditor({
        selector: '#editor-container',
        html: '<p><br></p>',
        config: editorConfig,
        mode: 'default', // or 'simple'
    })

    const toolbarConfig = {}

    const toolbar = createToolbar({
        editor,
        selector: '#toolbar-container',
        config: toolbarConfig,
        mode: 'default', // or 'simple'
    })

    $("#submit-btn").click(function (event) {
        event.preventDefault()
        let title = $("input[name='title']").val()
        let category = $("select[name='category']").val()
        let content = editor.getHtml()
        let csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val()
        $.ajax('/blog/pub', {
            method: 'POST',
            data: {title, category, content, csrfmiddlewaretoken},
            success: function (result) {
                let blog_id = result['data']['blog_id']
                // console.log(result)
                if (result['code'] == '200') {
                    window.location = '/blog/detail/' + blog_id

                }
                else{
                    alert(result['msg'])
                }
            }
        })
    })

}