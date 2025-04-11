// 生成粒子
function createParticles() {
    const container = document.getElementById('particles-container');
    const particleCount = 50; // 粒子数量

    for (let i = 0; i < particleCount; i++) {
        // 创建粒子
        const particle = document.createElement('div');
        particle.classList.add('particle');

        // 随机化粒子参数
        const size = Math.random() * 5 + 2; // 随机大小 (2px - 7px)
        const speed = Math.random() * 10 + 5; // 随机速度
        const distanceX = Math.random() * 300 - 150; // 随机水平漂浮距离
        const distanceY = Math.random() * 300 - 150; // 随机垂直漂浮距离
        const rotation = Math.random() * 45; // 随机旋转角度
        const blur = Math.random() * 2 + 1; // 随机模糊程度

        // 设置粒子样式
        particle.style.setProperty('--distance-x', `${distanceX}px`);
        particle.style.setProperty('--distance-y', `${distanceY}px`);
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.animationDuration = `${40 / speed}s`;
        particle.style.rotate = `${rotation}deg`;
        particle.style.filter = `blur(${blur}px)`;
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.top = `${Math.random() * 100}%`;

        // 添加到容器
        container.appendChild(particle);
    }
}

// 页面加载完成后生成粒子
window.onload = createParticles;