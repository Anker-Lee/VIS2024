<template>
    <!-- 这里写Html -->
    <div class="wrapper">
        <div v-show="!showMain" class="container">
            <div class="brand-section">
                <div class="header">DANCING BOARD</div>
                <div id="slogan">Turn your story into animated storyboard!</div>
            </div>
            <el-input type="textarea" :rows="50" placeholder="Please enter content" v-model="input_story"
                class="input-area">
            </el-input>
            <button class="generate-btn" :disabled="isButtonDisabled" @click="showMainPage">Generate your
                storyboard!</button>
        </div>


        <div v-show="showMain">
            <el-row :gutter="40">
                <el-col :span="7">
                    <div id="left_view">
                        <div class="header grid-content">DANCING BOARD</div>
                        <story></story>
                    </div>
                </el-col>
                <el-col :span="17">
                    <div id="storyboard" style="height: 1320px;">
                        <storyboard></storyboard>
                    </div>
                </el-col>
            </el-row>
        </div>

    </div>
</template>
<script src="./script.js"></script>
<style type="text/css">
/* 画布大小 2560*1440 */
.wrapper {
    width: 2440px;
    height: 1320px;
    border: 2px solid #22201420;
    /* border-bottom: none; */
    border-radius: 5px;
    padding: 60px;
    background: #FFFCF9;
    /* Add padding */

}

.container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    /* Adjust the ratio as needed */
    grid-template-rows: auto;
    gap: 20px;
    /* Space between grid items */
    align-items: center;
    padding: 20px;
}

.brand-section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    /* Aligns children to the center of the flex container */
    grid-column: 1 / 2;
}

.input-area {
    grid-column: 2 / 3;
    width: 100%;
    /* Full width of grid column */
    /* Adjust height if needed or use the rows attribute to define height */
}

.generate-btn {
    grid-column: 2 / 3;
    /* Span across both columns */
    justify-self: center;
    /* Center the button */
    margin-top: 60px;
    /* Space above the button */

    display: flex;
    width: 480px;
    height: 160px;
    padding: 5px 16px;
    justify-content: center;
    align-items: center;
    flex-shrink: 0;

    border-radius: 10px;

    color: var(--color-white, #FFF);
    text-align: center;
    font-family: Montserrat;
    font-size: 48px;
    font-style: italic;
    font-weight: 600;
    line-height: 26px;
    /* 54.167% */
}

.grid-content {
    border: 2px solid #22201420;
    border-radius: 5px;
}

#slogan {
    color: var(--color-black, #000);
    text-align: center;
    font-family: "Nothing You Could Do";
    font-size: 96px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;

    width: 953px;
    height: 256px;

    margin-block: 30px;
}

/* 标题 */
.header {
    width: 700px;
    height: 160px;
    flex-shrink: 0;
    border: 1px solid #000;
    background: #7566A9
}

.header {
    color: #fff;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: Montserrat;
    font-size: 80px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
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
./home.js./home.js
