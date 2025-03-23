window.onload = function() {
    function bindCaptchaBtnClick() {
            $("#captcha-btn").on("click", function(event) {
        let $this = $(this)
        let email = $("input[name='email']").val()
        if (!email){
            alert("请输入有效的邮箱！")
            return
        }
        $this.off("click")

        $.ajax('captcha/?email=' + email,{
            method: "GET",
            success: function(result){
                if (result['code'] == 200) {
                    alert("验证码发送成功！")
                }else {
                    alert(result['message'])
                }

            },
            fail: function(errpr){
                console.log(error)
            }
        })

        let countdown = 60
        let timer = setInterval(function() {
            if (countdown <= 0){
                $this.text('获取验证码')
                clearInterval(timer)
                bindCaptchaBtnClick()
            }
            else {
                $this.text(countdown+'s')
                countdown--
            }

        }, 1000)
    })
    }

    bindCaptchaBtnClick()

}