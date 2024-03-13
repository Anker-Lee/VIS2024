<template>
    <div id="app">
        <img id="emoji_1" class="emoji" src="../../assets/image/reshot-icon-disbelief-TQL2MNDFRK.svg" alt="emoji_1">
        <img id="emoji_2" class="emoji" src="../../assets/image/reshot-icon-disbelief-TQL2MNDFRK.svg" alt="emoji_1">
    </div>
</template>

<script>

import gsap from 'gsap';
import MotionPathPlugin from 'gsap/MotionPathPlugin';
import Draggable from 'gsap/src/Draggable';

gsap.registerPlugin(MotionPathPlugin, Draggable);

export default {
    mounted() {
        this.animateShape();
    },
    methods: {
        animateShape() {
            // const emojis = [emoji_1, emoji_2];

            let tl = gsap.timeline({ defaults: { duration: 2 } });


            tl.to("#emoji_1", { x: 300, rotation: 360, scale: 1.5 }) // 平移
                .to("#emoji_2", {
                    ease: "power1.inOut",  // 先加速后减速
                    // yoyo: true,
                    // repeat: -1,
                    motionPath: {
                        path: [
                            { x: 100, y: 0 },
                            { x: 600, y: 200 },
                            { x: 1000, y: 100 },
                            { x: 1400, y: 300 }
                        ],
                        curviness: 1.5,
                        autoRotate: true // 使目标在移动时自动沿路径方向旋转
                    },
                });

            Draggable.create("#emoji_1", {
                bounds: document.getElementById("storyboard"),
                inertia: true,
                onClick: function () {
                    console.log("clicked");
                },
                onDragEnd: function () {
                    console.log("drag ended");
                },
            });
        },
    },
};
</script>

<style>
.emoji {
    width: 100px;
    height: 100px;
}
</style>
