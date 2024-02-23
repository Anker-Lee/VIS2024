<template>
    <!-- 这里写Html -->
    <div class="wrapper">
        <el-row :gutter="10">
            <el-col :span="4">
                <div id="hxb_viz" class="grid-content ep-bg-purple" style="margin: 10px 0px 10px 10px">
                    <el-input v-model="inputMsg" placeholder="Say something..."></el-input>
                    <el-button @click="testBackend">Send</el-button>
                    <div id="chatResponse"></div>
                </div>
            </el-col>
            <el-col :span="16">
                <div class="grid-content ep-bg-purple" style="margin: 10px 0px">
                </div>
                <div class="grid-content ep-bg-purple" style="height: 1160px;">

                    <div class="grid-content-p" style="margin: 10px 0px; height: 410px; overflow-y: auto;">
                    </div>
                </div>
            </el-col>
            <el-col :span="4">
                <div class="grid-content ep-bg-purple" style="height: 400px; margin: 10px 10px 10px 0px">

                </div>
                <div class="grid-content ep-bg-purple" style="height:960px; margin: 10px 10px 10px 0px">
                </div>
            </el-col>
        </el-row>
    </div>
</template>
<script src="./script.js"></script>
<style type="text/css">
/* 画布大小 1920*1080 + 标题大小 1920 * 35 */
.wrapper {
    width: 2520px;
    height: 1550px;
    border: 2px solid #22201420;
    /* border-bottom: none; */
    border-radius: 5px;
}

.grid-content {
    border: 2px solid #22201420;
    /* border-bottom: none; */
    border-radius: 5px;
}

/* 标题FMLens */
.header {
    width: 270px;
    height: 116px;
    position: relative;
    left: 20px;
    top: 30px;
}

.title {
    width: 270px;
    height: 80px;
    position: relative;
    left: 20px;
    top: 20px;
    font: 40px "KaiseiOptiMedium";
}

.timeline {
    width: 2100px;
    height: 80px;
    position: absolute;
    left: 390px;
    top: 30px;
}

.group {
    width: 1998px;
    height: 1249px;
    position: absolute;
    left: -2px;
    /* border: 2px solid #d6d6d6; */
    border-top: none;
    border-right: none;
    border-bottom-left-radius: 5px;
}

.individual {
    width: 520px;
    height: 1249px;
    position: absolute;
    left: 1998px;
    /* border: 2px solid #d6d6d6; */
    border-top: none;
    border-left: none;
    border-bottom-right-radius: 5px;
}

.group_rect {
    height: 41px;
    width: 1838px;
    position: absolute;
    left: 0px;
    top: 0px;
    background: #b6433010;
    border-radius: 10px;
}

.group_title {
    width: 200px;
    height: 41px;
    position: absolute;
    left: 20px;
    top: 0px;
    font: 24px "KaiseiOptiMedium";
}

#groupLegend {
    width: 330px;
    height: 80px;
    position: absolute;
    right: 0px;
    top: 0px;
}

.individual_rect {
    height: 41px;
    width: 683px;
    position: absolute;
    left: 1838px;
    top: 0px;
    background: #d27d1c15;
    border-radius: 10px;
}

.individual_title {
    width: 200px;
    height: 41px;
    position: absolute;
    left: 20px;
    top: 0px;
    font: 24px "KaiseiOptiMedium";
}

/* 小标题 */
/* text, element-table */
text,
.el-table {
    font-family: "KaiseiOptiRegular";
}

/* 背景 */
.bg {
    /* height: 1025px; */
    background: #ffffff;
}

.el-loading-spinner .circular {
    width: 42px;
    height: 42px;
    animation: loading-rotate 2s linear infinite;
    stroke: #b6433070;
}

.el-loading-spinner .path {
    stroke: #b6433070 !important;
}

.el-loading-spinner .el-loading-text {
    color: #b6433070;
    font: 24px "KaiseiOptiRegular";
}

@font-face {
    font-family: "KaiseiOptiMedium";
    src: url("../../assets/font/kaisei-opti-medium.ttf");
}

@font-face {
    font-family: "KaiseiOptiRegular";
    src: url("../../assets/font/kaisei-opti-regular.ttf");
}

.el-col {
    border-radius: 4px;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}
</style>

