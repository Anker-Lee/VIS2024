<template>
    <div id="app" style="position: relative">
        <div
            style="position: absolute; width: 1600px; height: 400px; right: 0px; border-radius: 20px; border: 2px solid #B2AAD1;">
            <!-- 角色展示 -->
            <div id="design_board_character" style="top: 0px; left: 0px;">
                <div v-for="(character, index) in all_character_and_item[currentFrameIndex]['characters']" :key="index"
                    class="boarder_style preview_block" style="position: relative;">
                    <div class="emoji_head" :class="{ emoji_head_no_legs: character.selectedEmoji[4] === '' }">
                        {{ character.selectedEmoji[0] }}</div>
                    <div class="emoji_clothes" :class="{ emoji_clothes_no_legs: character.selectedEmoji[4] === '' }"> {{
                    character.selectedEmoji[2] }}</div>
                    <div class="emoji_left_hand"
                        :class="{ emoji_left_hand_no_legs: character.selectedEmoji[4] === '' }"> {{
                    character.selectedEmoji[1] }}</div>
                    <div class="emoji_right_hand"
                        :class="{ emoji_right_hand_no_legs: character.selectedEmoji[4] === '' }">
                        {{ character.selectedEmoji[3] }}</div>
                    <div class="emoji_pants">{{
                    character.selectedEmoji[4] }}</div>
                    <div class="emoji_left_foot">{{
                    character.selectedEmoji[5] }}</div>
                    <div class="emoji_right_foot">{{
                    character.selectedEmoji[6] }}</div>
                    <div class="color_block" style="position: absolute; top: 150px ">
                        <div class="preview_name" style="position: absolute; top: 0px; left: 30px">{{ character.name }}
                        </div>
                        <img class="preview_edit"
                            style="position: absolute; top: 5px; right: 5px; width: 40px; height: 40px;"
                            src="../../assets/image/icon_edit.svg" @click="changeEditPanelRec(index)" />
                    </div>
                </div>
            </div>

            <!-- 物品展示 -->
            <div id="design_board_items" style="top: 200px">
                <div v-for="(item, index) in all_character_and_item[currentFrameIndex]['items']" :key="index"
                    class="boarder_style preview_block" style="position: relative;">
                    <div class="emoji_item" style="position: absolute; top: 75px; left: 150px">{{ item.selectedEmoji }}
                    </div>
                    <div class="color_block" style="position: absolute; top: 150px ">
                        <div class="preview_name" style="position: absolute; top: 0px; left: 30px">{{ item.name }}
                        </div>
                        <img class="preview_edit"
                            style="position: absolute; top: 5px; right: 5px; width: 40px; height: 40px;"
                            src="../../assets/image/icon_edit.svg" @click="changeEditPanelRec_Item(index)" />
                    </div>

                </div>
            </div>
        </div>

        <!-- 角色编辑  -->
        <div v-for="(character, index) in all_character_and_item[currentFrameIndex]['characters']" :key="index"
            class="boarder_style edit_panel" style="position: absolute; top: 210px; right: 420px"
            v-show="showEditPanelRec[index]">
            <div class="edit_panel_title">Figure Editing -&nbsp;<span class="edit_panel_name">{{ character.name
                    }}</span>
                <img src="../../assets/image/check.svg" style="position: absolute; right: 40px;"
                    @click="changeEditPanelRec(index)" />
            </div>

            <div class="small_block_medium small_block"
                :class="{ small_block_selected: selectedBlock === 0, small_block_occupied: character.selectedEmoji[0] !== '' }"
                style="position: absolute; top: 190px; left: 220px;" @click=" clickBlock(0)">{{
                    character.selectedEmoji[0] }}</div>
            <div class="small_block_small small_block"
                :class="{ small_block_selected: selectedBlock === 1, small_block_occupied: character.selectedEmoji[1] !== '' }"
                style="position: absolute; top: 350px; left: 100px;" @click=" clickBlock(1)">{{
                    character.selectedEmoji[1] }}</div>
            <div class="small_block_large small_block "
                :class="{ small_block_selected: selectedBlock === 2, small_block_occupied: character.selectedEmoji[2] !== '' }"
                style="position: absolute; top: 350px; left: 200px;" @click=" clickBlock(2)">{{
                    character.selectedEmoji[2] }}</div>
            <div class="small_block_small small_block"
                :class="{ small_block_selected: selectedBlock === 3, small_block_occupied: character.selectedEmoji[3] !== '' }"
                style="position: absolute; top: 350px; left: 400px;" @click=" clickBlock(3)">{{
                    character.selectedEmoji[3] }}</div>
            <div class="small_block_medium small_block"
                :class="{ small_block_selected: selectedBlock === 4, small_block_occupied: character.selectedEmoji[4] !== '' }"
                style="position: absolute; top: 550px; left: 220px;" @click=" clickBlock(4)">{{
                    character.selectedEmoji[4] }}</div>
            <div class="small_block_small small_block"
                :class="{ small_block_selected: selectedBlock === 5, small_block_occupied: character.selectedEmoji[5] !== '' }"
                style="position: absolute; top: 710px; left: 184px;" @click=" clickBlock(5)">{{
                    character.selectedEmoji[5] }}</div>
            <div class="small_block_small small_block"
                :class="{ small_block_selected: selectedBlock === 6, small_block_occupied: character.selectedEmoji[6] !== '' }"
                style="position: absolute; top: 710px; left: 316px;" @click=" clickBlock(6)">{{
                    character.selectedEmoji[6] }}</div>

            <span class="title_inventory" style="position: absolute; top: 198px; left: 793px">Inventory</span>
            <div class="emoji_list" style="position: absolute; top: 300px; left: 600px">
                <span class="emoji_in_list" v-for="(e, i) in emojis[selectedBlock]" :key="i"
                    @click="changeEmoji(i, index)">{{ e
                    }}</span>
            </div>
            <div class="edit_panel_bt_container" style="position: absolute; left: 1225px; top: 624px">
                <img src="../../assets/image/FolderAdd.svg" class="edit_panel_button" />
                <img src="../../assets/image/circle-close.svg" class="edit_panel_button" @click="removeEmoji(index)" />
            </div>
        </div>

        <!-- 物品编辑 -->
        <div v-for="(item, index) in all_character_and_item[currentFrameIndex]['items']" :key="index + 100"
            class="boarder_style edit_panel" style="position: absolute; top: 210px; right: 420px"
            v-show="showEditPanelRec_item[index]">
            <div class="edit_panel_title">Figure Editing -&nbsp;<span class="edit_panel_name">{{ item.name }}</span>
                <img src="../../assets/image/check.svg" style="position: absolute; right: 40px;"
                    @click="changeEditPanelRec_Item(index)" />
            </div>

            <div class="small_block small_block_XLarge"
                :class="{ small_block_selected: selectedBlock_item === 1, small_block_occupied: item.selectedEmoji !== '' }"
                style="position: absolute; top: 380px; left: 180px;" @click="clickBlockItem">{{ item.selectedEmoji }}
            </div>

            <span class="title_inventory" style="position: absolute; top: 198px; left: 793px">Inventory</span>
            <div class="emoji_list" style="position: absolute; top: 300px; left: 600px">
                <span class="emoji_in_list" v-for="(e, i) in emojis_item" :key="i"
                    @click="changeEmoji_Item(e, index)">{{ e }}</span>
            </div>
            <div class="edit_panel_bt_container" style="position: absolute; left: 1225px; top: 624px">
                <img src="../../assets/image/FolderAdd.svg" class="edit_panel_button" />
                <img src="../../assets/image/circle-close.svg" class="edit_panel_button"
                    @click="removeEmoji_item(index)" />
            </div>
        </div>


        <!-- 故事板 -->
        <div id="story_board" style="position: absolute; top: 420px; right: 100px;">

            <img id="emoji_1" class="emoji" src="../../assets/image/reshot-icon-disbelief-TQL2MNDFRK.svg" alt="emoji_1">

            <div v-for="(character, index) in all_character_and_item[currentFrameIndex]['characters']"
                :key="index + 300" :id="'character-' + index" class="character_in_story"
                style="position: absolute; top: 10px; left: 10px;" @click="handle_emoji_click($event)">
                <div class="emoji_head emoji_click" :class="{ emoji_head_no_legs: character.selectedEmoji[4] === '' }"
                    :id="'head_' + index">
                    {{ character.selectedEmoji[0] }}</div>
                <div class="emoji_clothes emoji_click"
                    :class="{ emoji_clothes_no_legs: character.selectedEmoji[4] === '' }" :id="'clothes_' + index"> {{
                    character.selectedEmoji[2] }}</div>
                <div class="emoji_left_hand emoji_click"
                    :class="{ emoji_left_hand_no_legs: character.selectedEmoji[4] === '' }" :id="'left_hand_' + index">
                    {{
                    character.selectedEmoji[1] }}</div>
                <div class="emoji_right_hand emoji_click"
                    :class="{ emoji_right_hand_no_legs: character.selectedEmoji[4] === '' }"
                    :id="'right_hand_' + index">
                    {{ character.selectedEmoji[3] }}</div>
                <div class="emoji_pants emoji_click" :id="'pants_' + index" v-if="character.selectedEmoji[4] !== ''">{{
                    character.selectedEmoji[4] }}</div>
                <div class="emoji_left_foot emoji_click" :id="'left_foot_' + index"
                    v-if="character.selectedEmoji[4] !== ''">{{
                    character.selectedEmoji[5] }}</div>
                <div class="emoji_right_foot emoji_click" :id="'right_foot_' + index"
                    v-if="character.selectedEmoji[4] !== ''">{{
                    character.selectedEmoji[6] }}</div>
            </div>

            <div v-for="(item, index) in all_character_and_item[currentFrameIndex]['items']" :key="index + 400"
                :id="'item-' + index" class="item_in_story emoji_item emoji_click"
                style="position: absolute; top: 50%; left: 50%;" @click="handle_emoji_click($event)">
                {{ item.selectedEmoji }}
            </div>


        </div>

        <!-- 动画顺序列表 -->
        <div style="position: absolute; top: 420px; right: 100px" class="animation_list grid-content"
            v-show="showAnimationList">
            <div class="animation_list_title">Frame {{ currentFrameIndex + 1 }} Animation</div>
            <div v-for="(animationSmallList, index) in all_animationList[currentFrameIndex]" :key="index"
                class="animation_item">
                <div style="width: 600px; height: 100px; background: #AF99C7;">
                    <div style="position: absolute; left: 0px" class="animation_title_index"> {{ index + 1 }}</div>
                    <div style="position: absolute; right: 0px" class="animation_title">{{
                    all_svo_list[currentFrameIndex][index] }}</div>
                </div>

                <div v-for="(animation, i) in animationSmallList" :key="i" class="animation_subaction">
                    {{ animation['name'] }}
                </div>
            </div>
        </div>

        <!-- 控制按钮 -->
        <div id="control" style="position: absolute; top: 420px; right: 0px">
            <img class="control_button " style="position: absolute; top: 0px;" src="../../assets/image/icon_edit.svg"
                v-if="isPlay" @click="isPlay = !isPlay" />
            <img class="control_button " style="position: absolute; top: 200px;" src="../../assets/image/Frame.svg"
                v-if="isPlay" @click="showAnimationList = !showAnimationList" />
            <img class="control_button " style="position: absolute; top: 500px;" src="../../assets/image/icon_play.svg"
                v-if="isPlay" @click="runAnimations()" />
            <img class="control_button " style="position: absolute; top: 600px;" src="../../assets/image/replay.svg"
                v-if="isPlay" />
            <img class="control_button " style="position: absolute; top: 800px;" src="../../assets/image/share.svg"
                v-if="isPlay" />


            <img class="control_button " style="position: absolute; top: 0px;" src="../../assets/image/check.svg"
                v-if="!isPlay" @click="isPlay = !isPlay" />
            <img class="control_button " style="position: absolute; top: 300px;" @click="customizeMove(lastClicked)"
                src="../../assets/image/ao/pathmovement.svg" v-if="!isPlay" />
            <img class="control_button " style="position: absolute; top: 400px;" @click="ao_scale(lastClicked)"
                src="../../assets/image/ao/scale.svg" v-if="!isPlay" />
            <img class="control_button " style="position: absolute; top: 500px;" @click="ao_rotation(lastClicked)"
                src="../../assets/image/ao/rotation.svg" v-if="!isPlay" />
            <img class="control_button " style="position: absolute; top: 600px;" @click="ao_flip(lastClicked)"
                src="../../assets/image/ao/flip.svg" v-if="!isPlay" />
            <img class="control_button " style="position: absolute; top: 700px;" @click="ao_appear(lastClicked)"
                src="../../assets/image/ao/appear.svg" v-if="!isPlay" />
            <img class="control_button " style="position: absolute; top: 800px;" @click="ao_disappear(lastClicked)"
                src="../../assets/image/ao/disappear.svg" v-if="!isPlay" />
        </div>

        <!-- 测试按钮 -->
        <div style="position: absolute; top: 1320px; left: 0px">
            <div class="control_button boarder_style test" style="position: absolute; top: 0px;"
                @click="ptrans(lastClicked, 'emoji_1')">移动到emoji</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 40px;"
                @click="propel_pull(lastClicked, 'emoji_1')">拉 emoji</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 0px; left: 80px"
                @click="move_head(lastClicked)">摇头</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 20px; left: 80px"
                @click="ingest(lastClicked, 'emoji_1')">吸入</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 40px; left: 80px"
                @click="expel(lastClicked, 'emoji_1')">排出</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 0px; left: 160px"
                @click="speak(lastClicked, 'Hello')">说话</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 20px; left: 160px"
                @click="atrans('character-0', 'character-1', 'emoji_1')">atrans</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 40px; left: 160px"
                @click="thought(lastClicked, 'Hello')">思考</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 60px; left: 160px"
                @click="thought_2(lastClicked, 'Hello')">思考2</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 0px; left: 240px"
                @click="scream(lastClicked, 'Hello')">尖叫</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 20px; left: 240px"
                @click="shake(lastClicked)">抖动</div>
            <div class="control_button boarder_style test" style="position: absolute; top:40px; left: 240px"
                @click="rotateHand(lastClicked)">转手</div>
            <div class="control_button boarder_style test" style="position: absolute; top:60px; left: 240px"
                @click="waveHand(lastClicked)">挥手</div>
            <div class="control_button boarder_style test" style="position: absolute; top:0px; left: 320px"
                @click="kickFoot(lastClicked)">踢</div>
            <div class="control_button boarder_style test" style="position: absolute; top:20px; left: 320px"
                @click="jump(lastClicked)">跳</div>
            <div class="control_button boarder_style test" style="position: absolute; top:40px; left: 320px"
                @click="walk(lastClicked)">走</div>
            <div class="control_button boarder_style test" style="position: absolute; top:60px; left: 320px"
                @click="node_head(lastClicked)">点头</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 0px; left: 400px"
                @click="cry(lastClicked)">流泪</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 20px; left: 400px"
                @click="runAnimations()">连续运行</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 40px; left: 400px"
                @click="saveScene()">存储场景</div>
                <div class="control_button boarder_style test" style="position: absolute; top: 60px; left: 400px"
                @click="loadScene()">恢复场景</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 0px; left: 480px"
                @click="clearUserAnimationsCache()">撤销</div>
            <div class="control_button boarder_style test" style="position: absolute; top: 20px; left: 480px"
                @click="confirmUserAnimations()">确认</div>
        </div>
    </div>
</template>

<script>

import gsap from 'gsap';
import MotionPathPlugin from 'gsap/MotionPathPlugin';
import Draggable from 'gsap/src/Draggable';

gsap.registerPlugin(MotionPathPlugin, Draggable);

export default {
    data() {
        return {
            emojis: [
                [
                    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲", "🥹", "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸", "🥳", "😏", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣", "😖", "😫", "😩", "🥺", "😢", "😭", "😮‍💨", "😤", "😠", "😡", "🤬", "🤯", "😳", "🥵", "🥶", "😱", "😨", "😰", "😥", "😓", "🫣", "🤗", "🫡", "🤔", "🫢", "🤭", "🤫", "🤥", "😶", "😶‍🌫️", "😐", "😑", "😬", "🫨", "🫠", "🙄", "😯", "😦", "😧", "😮", "😲", "🥱", "😴", "🤤", "😪", "😵", "😵‍💫", "🫥", "🤐", "🥴", "🤢", "🤮", "🤧", "😷", "🤒", "🤕", "🤑", "🤠", "😈", "👿", "👹", "👺", "🤡", "💩", "👻", "💀", "☠️", "👽", "👾", "🎃", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾", "👶", "👧", "🧒", "👦", "👩", "🧑", "👨", "👩‍🦱", "🧑‍🦱", "👨‍🦱", "👩‍🦰", "🧑‍🦰", "👨‍🦰", "👱‍♀️", "👱", "👱‍♂️", "👩‍🦳", "🧑‍🦳", "👨‍🦳", "👩‍🦲", "🧑", "👨‍🦲", "🧔‍♀️", "🧔", "🧔‍♂️", "👵", "🧓", "👴", "👲", "👳‍♀️", "👳", "👳‍♂️", "🧕", "👮‍♀️", "👮", "👮‍♂️", "👷‍♀️", "👷", "👷‍♂️", "💂‍♀️", "💂", "💂‍♂️", "🕵️‍♀️", "🕵️", "🕵️‍♂️", "👩‍⚕️", "🧑‍⚕️", "👨‍⚕️", "👩‍🌾", "🧑‍🌾", "👨", "👩‍🍳", "🧑‍🍳", "👨‍🍳", "👩‍🎓", "🧑‍🎓", "👨‍🎓", "👩‍🎤", "🧑‍🎤", "👨‍🎤", "👩‍🏫", "🧑‍🏫", "👨‍🏫", "👩‍🏭", "🧑‍🏭", "👨‍🏭", "👩‍💻", "🧑‍💻", "👨‍💻", "👩‍💼", "🧑‍💼", "👨‍💼", "👩‍🔧", "🧑‍🔧", "👨‍🔧", "👩", "🧑‍🔬", "👨‍🔬", "👩‍🎨", "🧑‍🎨", "👨‍🎨", "👩‍🚒", "🧑‍🚒", "👨‍🚒", "👩‍✈️", "🧑‍✈️", "👨‍✈️", "👩‍🚀", "🧑‍🚀", "👨‍🚀", "👩‍⚖️", "🧑‍⚖️", "👨‍⚖️", "👰‍♀️", "👰", "👰‍♂️", "🤵‍♀️", "🤵", "🤵‍♂️", "👸", "🫅", "🤴", "🥷", "🦸‍♀️", "🦸", "🦸‍♂️", "🦹‍♀️", "🦹", "🦹‍♂️", "🤶", "🧑‍🎄", "🎅", "🧙‍♀️", "🧙", "🧙‍♂️", "🧝‍♀️", "🧝", "🧝‍♂️", "🧛‍♀️", "🧛", "🧛‍♂️", "🧟‍♀️", "🧟", "🧟‍♂️", "👼", "🙎‍♀️", "🙎", "🙎‍♂️", "🙍‍♀️", "🙍", "🙍‍♂️", "💇‍♀️", "💇", "💇‍♂️", "💆‍♀️", "💆", "💆‍♂️", "🧖‍♀️", "🧖", "🧖‍♂️", "👶🏻", "👧🏻", "🧒🏻", "👦🏻", "👩🏻", "🧑🏻", "👨🏻", "👩🏻‍🦱", "🧑🏻‍🦱", "👨🏻‍🦱", "👩🏻‍🦰", "🧑🏻‍🦰", "👨🏻‍🦰", "👱🏻‍♀️", "👱🏻", "👱🏻‍♂️", "👩🏻‍🦳", "🧑🏻‍🦳", "👨🏻‍🦳", "👩🏻‍🦲", "🧑🏻‍🦲", "👨🏻", "🧔🏻‍♀️", "🧔🏻", "🧔🏻‍♂️", "👵🏻", "🧓🏻", "👴🏻", "👲🏻", "👳🏻‍♀️", "👳🏻", "👳🏻‍♂️", "🧕🏻", "👮🏻‍♀️", "👮🏻", "👮🏻‍♂️", "👷🏻‍♀️", "👷🏻", "👷🏻‍♂️", "💂🏻‍♀️", "💂🏻", "💂🏻‍♂️", "🕵🏻‍♀️", "🕵🏻", "🕵🏻‍♂️", "👩🏻‍⚕️", "🧑🏻‍⚕️", "👨🏻‍⚕️", "👩🏻‍🌾", "🧑🏻‍🌾", "👨🏻‍🌾", "👩🏻‍🍳", "🧑🏻‍🍳", "👨🏻‍🍳", "👩🏻‍🎓", "🧑🏻‍🎓", "👨🏻‍🎓", "🧑🏻‍🎤", "👨🏻‍🎤", "👩🏻‍🏫", "🧑🏻‍🏫", "👨🏻‍🏫", "🧑🏻‍🏭", "👨🏻‍🏭", "👩🏻‍💻", "🧑🏻‍💻", "👨🏻‍💻", "👩🏻‍💼", "🧑🏻‍💼", "👨🏻‍💼", "👩🏻‍🔧", "🧑🏻‍🔧", "👨🏻‍🔧", "👩🏻‍🔬", "🧑🏻‍🔬", "👨🏻‍🔬", "👩🏻‍🎨", "🧑🏻‍🎨", "👨🏻‍🎨", "👩🏻‍🚒", "👨🏻‍🚒", "👩🏻‍✈️", "🧑🏻‍✈️", "👨🏻‍✈️", "👩🏻‍🚀", "👨🏻‍🚀", "👩🏻‍⚖️", "🧑🏻‍⚖️", "👨🏻‍⚖️", "👰🏻‍♀️", "👰🏻", "👰🏻‍♂️", "🤵🏻‍♀️", "🤵🏻", "🤵🏻‍♂️", "👸🏻", "🫅🏻", "🤴🏻", "🥷🏻", "🦸🏻", "🦸🏻‍♂️", "🦹🏻‍♀️", "🦹🏻", "🦹🏻‍♂️", "🤶🏻", "🧑🏻‍🎄", "🎅🏻", "🧙🏻‍♀️", "🧙🏻", "🧙🏻‍♂️", "🧝🏻‍♀️", "🧝🏻", "🧝🏻‍♂️", "🧛🏻‍♀️", "🧛🏻", "🧛🏻‍♂️", "💁🏻‍♀️", "💁🏻", "💁🏻‍♂️", "🙅🏻‍♀️", "🙅🏻", "🙅🏻‍♂️", "🙆🏻‍♀️", "🙆🏻", "🙆🏻‍♂️", "🙋🏻‍♀️", "🙋🏻", "🙋🏻‍♂️", "🧏🏻‍♀️", "🧏🏻", "🤦🏻‍♀️", "🤦🏻", "🤦🏻‍♂️", "🤷🏻‍♀️", "🤷🏻", "🤷🏻‍♂️", "🙎🏻", "🙎🏻‍♂️", "🙍🏻‍♀️", "🙍🏻", "🙍🏻‍♂️", "💇🏻‍♀️", "💇", "💇🏻‍♂️", "💆🏻‍♀️", "💆🏻", "💆🏻‍♂️", "🧖🏻‍♀️", "🧖🏻", "🧖🏻‍♂️", "👶🏼", "👧🏼", "🧒🏼", "👦🏼", "👩🏼", "🧑🏼", "👨🏼", "👩🏼‍🦱", "🧑🏼‍🦱", "👨🏼‍🦱", "👩🏼‍🦰", "🧑🏼‍🦰", "👨🏼‍🦰", "👱🏼‍♀️", "👱🏼", "👱🏼‍♂️", "👩🏼‍🦳", "🧑🏼‍🦳", "👨🏼‍🦳", "👩🏼‍🦲", "🧑🏼‍🦲", "👨🏼", "🧔🏼‍♀️", "🧔🏼", "🧔🏼‍♂️", "👵🏼", "🧓🏼", "👴🏼", "👲🏼", "👳🏼‍♀️", "👳🏼", "👳🏼‍♂️", "🧕🏼", "👮🏼‍♀️", "👮🏼", "👮🏼‍♂️", "👷🏼‍♀️", "👷🏼", "👷🏼‍♂️", "💂🏼‍♀️", "💂🏼", "💂🏼‍♂️", "🕵🏼‍♀️", "🕵🏼", "🕵🏼‍♂️", "👩🏼‍⚕️", "🧑🏼‍⚕️", "👨🏼‍⚕️", "👩🏼‍🌾", "🧑🏼‍🌾", "👨🏼‍🌾", "👩🏼‍🍳", "🧑🏼‍🍳", "👨🏼‍🍳", "👩🏼‍🎓", "🧑🏼‍🎓", "👨🏼‍🎓", "🧑🏼‍🎤", "👨🏼‍🎤", "👩🏼‍🏫", "🧑🏼‍🏫", "👨🏼‍🏫", "🧑🏼‍🏭", "👨🏼‍🏭", "👩🏼‍💻", "🧑🏼‍💻", "👨🏼‍💻", "👩🏼‍💼", "🧑🏼‍💼", "👨🏼‍💼", "👩🏼‍🔧", "🧑🏼‍🔧", "👨🏼‍🔧", "👩🏼‍🔬", "🧑🏼‍🔬", "👨🏼‍🔬", "👩🏼‍🎨", "🧑🏼‍🎨", "👨🏼‍🎨", "👩🏼‍🚒", "👨🏼‍🚒", "👩🏼‍✈️", "🧑🏼‍✈️", "👨🏼‍✈️", "👩🏼‍🚀", "👨🏼‍🚀", "👩🏼‍⚖️", "🧑🏼‍⚖️", "👨🏼‍⚖️", "👰🏼‍♀️", "👰🏼", "👰🏼‍♂️", "🤵🏼‍♀️", "🤵🏼", "🤵🏼‍♂️", "👸🏼", "🫅🏼", "🤴🏼", "🥷🏼", "🦸🏼", "🦸🏼‍♂️", "🦹🏼‍♀️", "🦹🏼", "🦹🏼‍♂️", "🤶🏼", "🧑🏼‍🎄", "🎅🏼", "🧙🏼‍♀️", "🧙🏼", "🧙🏼‍♂️", "🧝🏼‍♀️", "🧝🏼", "🧝🏼‍♂️", "🧛🏼‍♀️", "🧛🏼", "🧛🏼‍♂️", "🙇🏼‍♀️", "🙇🏼", "🙇🏼‍♂️", "💁🏼‍♀️", "💁🏼", "💁🏼‍♂️", "🙅🏼‍♀️", "🙅🏼", "🙅🏼‍♂️", "🙆🏼‍♀️", "🙆🏼", "🙆🏼‍♂️", "🙋🏼‍♀️", "🙋🏼", "🧏🏼‍♀️", "🧏🏼", "🧏🏼‍♂️", "🤦🏼‍♀️", "🤦🏼", "🤦🏼‍♂️", "🤷🏼", "🤷🏼‍♂️", "🙎🏼‍♀️", "🙎🏼", "🙎🏼‍♂️", "🙍🏼‍♀️", "🙍🏼‍♂️", "💇🏼‍♀️", "💇🏼", "💇🏼‍♂️", "💆🏼‍♀️", "💆🏼", "💆🏼‍♂️", "🧖🏼‍♀️", "🧖🏼", "🧖🏼‍♂️", "👶🏽", "👧🏽", "🧒🏽", "👦🏽", "👩🏽", "🧑🏽", "👨🏽", "👩🏽‍🦱", "🧑🏽‍🦱", "👨🏽‍🦱", "👩🏽‍🦰", "🧑🏽‍🦰", "👨🏽‍🦰", "👱🏽‍♀️", "👱🏽", "👱🏽‍♂️", "👩🏽‍🦳", "🧑🏽‍🦳", "👨🏽‍🦳", "👩🏽‍🦲", "🧑🏽‍🦲", "👨🏽", "🧔🏽‍♀️", "🧔🏽", "🧔🏽‍♂️", "👵🏽", "🧓🏽", "👴🏽", "👲🏽", "👳🏽‍♀️", "👳🏽", "👳🏽‍♂️", "🧕🏽", "👮🏽‍♀️", "👮🏽", "👮🏽‍♂️", "👷🏽‍♀️", "👷🏽", "👷🏽‍♂️", "💂🏽‍♀️", "💂🏽", "💂🏽‍♂️", "🕵🏽‍♀️", "🕵🏽", "🕵🏽‍♂️", "👩🏽‍⚕️", "🧑🏽‍⚕️", "👨🏽‍⚕️", "👩🏽‍🌾", "🧑🏽‍🌾", "👨🏽‍🌾", "👩🏽‍🍳", "🧑🏽‍🍳", "👨🏽‍🍳", "👩🏽‍🎓", "🧑🏽‍🎓", "👨🏽‍🎓", "🧑🏽‍🎤", "👨🏽‍🎤", "👩🏽‍🏫", "🧑🏽‍🏫", "👨🏽‍🏫", "🧑🏽‍🏭", "👨🏽‍🏭", "👩🏽‍💻", "🧑🏽‍💻", "👨🏽‍💻", "👩🏽‍💼", "🧑🏽‍💼", "👨🏽‍💼", "👩🏽‍🔧", "🧑🏽‍🔧", "👨🏽‍🔧", "👩🏽‍🔬", "🧑🏽‍🔬", "👨🏽‍🔬", "👩🏽‍🎨", "🧑🏽‍🎨", "👨🏽‍🎨", "👩🏽‍🚒", "👨🏽‍🚒", "👩🏽‍✈️", "🧑🏽‍✈️", "👨🏽‍✈️", "👩🏽‍🚀", "👨🏽‍🚀", "👩🏽‍⚖️", "🧑🏽‍⚖️", "👨🏽‍⚖️", "👰🏽‍♀️", "👰🏽", "👰🏽‍♂️", "🤵🏽‍♀️", "🤵🏽", "🤵🏽‍♂️", "👸🏽", "🫅🏽", "🤴🏽", "🥷🏽", "🦸🏽", "🦸🏽‍♂️", "🦹🏽‍♀️", "🦹🏽", "🦹🏽‍♂️", "🤶🏽", "🧑🏽‍🎄", "🎅🏽", "🧙🏽‍♀️", "🧙🏽", "🧙🏽‍♂️", "🧝🏽‍♀️", "🧝🏽", "🧝🏽‍♂️", "🧛🏽‍♀️", "🧛🏽", "🧛🏽‍♂️", "🧜🏽‍♀️", "🧜🏽", "🧜🏽‍♂️", "🧚🏽‍♀️", "🧚🏽", "🧚🏽‍♂️", "👼🏽", "🤰🏽", "🫄🏽", "🫃🏽", "🤱🏽", "👩🏽‍🍼", "👨🏽‍🍼", "🙇🏽‍♀️", "🙇🏽", "🙇🏽‍♂️", "💁🏽‍♀️", "💁🏽", "🙅🏽‍♀️", "🙅🏽", "🙅🏽‍♂️", "🙆🏽‍♀️", "🙆🏽", "🙆🏽‍♂️", "🙋🏽", "🙋🏽‍♂️", "🧏🏽‍♀️", "🧏🏽", "🧏🏽‍♂️", "🤦🏽‍♀️", "🤦🏽‍♂️", "🤷🏽‍♀️", "🤷🏽", "🤷🏽‍♂️", "🙎🏽‍♀️", "🙎🏽", "🙎🏽‍♂️", "🙍🏽‍♀️", "🙍🏽", "🙍🏽‍♂️", "💇🏽‍♀️", "💇🏽", "💇🏽‍♂️", "💆🏽‍♀️", "💆🏽", "💆🏽‍♂️", "🧖🏽‍♀️", "🧖🏽", "🧖🏽‍♂️", "👶🏾", "👧🏾", "🧒🏾", "👦🏾", "👩🏾", "🧑🏾", "👨🏾", "👩🏾‍🦱", "🧑🏾‍🦱", "👨🏾‍🦱", "👩🏾‍🦰", "🧑🏾‍🦰", "👨🏾‍🦰", "👱🏾‍♀️", "👱🏾", "👱🏾‍♂️", "👩🏾‍🦳", "🧑🏾‍🦳", "👨🏾‍🦳", "👩🏾‍🦲", "🧑🏾‍🦲", "👨🏾", "🧔🏾‍♀️", "🧔🏾", "🧔🏾‍♂️", "👵🏾", "🧓🏾", "👴🏾", "👲🏾", "👳🏾‍♀️", "👳🏾", "👳🏾‍♂️", "🧕🏾", "👮🏾‍♀️", "👮🏾", "👮🏾‍♂️", "👷🏾‍♀️", "👷🏾", "👷🏾‍♂️", "💂🏾‍♀️", "💂🏾", "💂🏾‍♂️", "🕵🏾‍♀️", "🕵🏾", "🕵🏾‍♂️", "👩🏾‍⚕️", "🧑🏾‍⚕️", "👨🏾‍⚕️", "👩🏾‍🌾", "🧑🏾‍🌾", "👨🏾‍🌾", "👩🏾‍🍳", "🧑🏾‍🍳", "👨🏾‍🍳", "👩🏾‍🎓", "🧑🏾‍🎓", "👨🏾‍🎓", "🧑🏾‍🎤", "👨🏾‍🎤", "👩🏾‍🏫", "🧑🏾‍🏫", "👨🏾‍🏫", "🧑🏾‍🏭", "👨🏾‍🏭", "👩🏾‍💻", "🧑🏾‍💻", "👨🏾‍💻", "👩🏾‍💼", "🧑🏾‍💼", "👨🏾‍💼", "👩🏾‍🔧", "🧑🏾‍🔧", "👨🏾‍🔧", "👩🏾‍🔬", "🧑🏾‍🔬", "👨🏾‍🔬", "👩🏾‍🎨", "🧑🏾‍🎨", "👨🏾‍🎨", "👩🏾‍🚒", "👨🏾‍🚒", "👩🏾‍✈️", "🧑🏾‍✈️", "👨🏾‍✈️", "👩🏾‍🚀", "👨🏾‍🚀", "👩🏾‍⚖️", "🧑🏾‍⚖️", "👨🏾‍⚖️", "👰🏾‍♀️", "👰🏾", "👰🏾‍♂️", "🤵🏾‍♀️", "🤵🏾", "🤵🏾‍♂️", "👸🏾", "🫅🏾", "🤴🏾", "🥷🏾", "🦸🏾", "🦸🏾‍♂️", "🦹🏾‍♀️", "🦹🏾", "🦹🏾‍♂️", "🤶🏾", "🧑🏾‍🎄", "🎅🏾", "🧙🏾‍♀️", "🧙🏾", "🧙🏾‍♂️", "🧝🏾‍♀️", "🧝🏾", "🧝🏾‍♂️", "🧛🏾‍♀️", "🧛🏾", "🧛🏾‍♂️", "🧜🏾‍♀️", "🧜🏾", "🧜🏾‍♂️", "🧚🏾‍♀️", "🧚🏾", "🧚🏾‍♂️", "👼🏾", "🤰🏾", "🫄🏾", "🫃🏾", "🤱🏾", "👩🏾‍🍼", "👨🏾‍🍼", "🙇🏾‍♀️", "🙇🏾", "🙇🏾‍♂️", "💁🏾‍♀️", "💁🏾", "🙅🏾‍♀️", "🙅🏾", "🙅🏾‍♂️", "🙆🏾‍♀️", "🙆🏾", "🙆🏾‍♂️", "🙋🏾", "🙋🏾‍♂️", "🧏🏾‍♀️", "🧏🏾", "🧏🏾‍♂️", "🤦🏾‍♀️", "🤦🏾‍♂️", "🤷🏾‍♀️", "🤷🏾", "🤷🏾‍♂️", "🙎🏾‍♀️", "🙎🏾", "🙎🏾‍♂️", "🙍🏾‍♀️", "🙍🏾", "🙍🏾‍♂️", "💇🏾‍♀️", "💇🏾", "💇🏾‍♂️", "💆🏾‍♀️", "💆🏾", "💆🏾‍♂️", "🧖🏾‍♀️", "🧖🏾", "🧖🏾‍♂️", "👶🏿", "👧🏿", "🧒🏿", "👦🏿", "👩🏿", "🧑🏿", "👨🏿", "👩🏿‍🦱", "🧑🏿", "👨🏿‍🦱", "👩🏿‍🦰", "🧑🏿‍🦰", "👨🏿‍🦰", "👱🏿‍♀️", "👱🏿", "👩🏿‍🦳", "🧑🏿‍🦳", "👨🏿‍🦳", "👩🏿‍🦲", "🧑🏿‍🦲", "👨🏿‍🦲", "🧔🏿‍♀️", "🧔🏿", "🧔🏿‍♂️", "👵🏿", "🧓🏿", "👴🏿", "👲🏿", "👳🏿‍♀️", "👳🏿", "👳🏿‍♂️", "🧕🏿", "👮🏿‍♀️", "👮🏿", "👮🏿‍♂️", "👷🏿‍♀️", "👷🏿‍♂️", "💂🏿‍♀️", "💂🏿", "💂🏿‍♂️", "🕵🏿‍♀️", "🕵🏿", "🕵🏿‍♂️", "👩🏿‍⚕️", "🧑🏿‍⚕️", "👨🏿‍⚕️", "👩🏿‍🌾", "🧑🏿‍🌾", "👨🏿", "👩🏿‍🍳", "🧑🏿‍🍳", "👨🏿‍🍳", "👩🏿‍🎓", "🧑🏿‍🎓", "👨🏿‍🎓", "👩🏿‍🎤", "🧑🏿‍🎤", "👨🏿‍🎤", "👩🏿‍🏫", "🧑🏿‍🏫", "👨🏿‍🏫", "👩🏿‍🏭", "🧑🏿‍🏭", "👨🏿‍🏭", "👩🏿‍💻", "🧑🏿‍💻", "👨🏿‍💻", "👩🏿‍💼", "🧑🏿‍💼", "👨🏿‍💼", "👩🏿‍🔧", "🧑🏿‍🔧", "👨🏿‍🔧", "👩🏿", "🧑🏿‍🔬", "👨🏿‍🔬", "👩🏿‍🎨", "🧑🏿‍🎨", "👨🏿‍🎨", "👩🏿‍🚒", "🧑🏿‍🚒", "👨🏿‍🚒", "👩🏿‍✈️", "🧑🏿‍✈️", "👨🏿‍✈️", "👩🏿‍🚀", "🧑🏿‍🚀", "👨🏿‍🚀", "👩🏿‍⚖️", "🧑🏿‍⚖️", "👨🏿‍⚖️", "👰🏿‍♀️", "👰🏿", "👰🏿‍♂️", "🤵🏿‍♀️", "🤵🏿", "🤵🏿‍♂️", "👸🏿", "🫅🏿", "🤴🏿", "🥷🏿", "🦸🏿‍♀️", "🦸🏿", "🦸🏿‍♂️", "🦹🏿‍♀️", "🦹🏿", "🦹🏿‍♂️", "🤶🏿", "🎅🏿", "🧙🏿‍♀️", "🧙🏿", "🧙🏿‍♂️", "🧝🏿‍♀️", "🧝🏿", "🧝🏿‍♂️", "🧛🏿‍♀️", "🧛🏿", "🧛🏿‍♂️", "🧜🏿‍♀️", "🧜🏿", "🧜🏿‍♂️", "🧚🏿‍♀️", "🧚🏿", "🧚🏿‍♂️", "👼🏿", "🤰🏿", "🫄🏿", "🫃🏿", "🤱🏿", "👩🏿‍🍼", "🧑🏿‍🍼", "👨🏿‍🍼", "🙇🏿‍♀️", "🙇🏿", "🙇🏿‍♂️", "💁🏿‍♀️", "💁🏿", "💁🏿‍♂️", "🙅🏿‍♀️", "🙅🏿", "🙅🏿‍♂️", "🙆🏿‍♀️", "🙆🏿", "🙆🏿‍♂️", "🙋🏿‍♀️", "🙋🏿", "🙋🏿‍♂️", "🧏🏿‍♀️", "🧏🏿", "🧏🏿‍♂️", "🤦🏿‍♀️", "🤦🏿", "🤦🏿‍♂️", "🤷🏿‍♀️", "🤷🏿", "🤷🏿‍♂️", "🙎🏿‍♀️", "🙎🏿", "🙎🏿‍♂️", "🙍🏿‍♀️", "🙍🏿", "🙍🏿‍♂️", "💇🏿‍♀️", "💇🏿", "💇🏿‍♂️", "💆🏿‍♀️", "💆🏿", "💆🏿‍♂️", "🧖🏿‍♀️", "🧖🏿", "🧖🏿‍♂️", "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐻‍❄️", "🐨", "🐯", "🦁", "🐮", "🐷", "🐽", "🐸", "🐵", "🙈", "🙉", "🙊", "🐔", "🐧", "🐦", "🐦‍⬛", "🐤", "🐣", "🐥", "🦆", "🦅", "🦉", "🦇", "🐺", "🐗", "🐴", "🦄", "🐝"],
                [
                    "👋", "🤚", "🖐", "✋", "🖖", "👌", "🤌", "🤏", "✌️", "🤞", "🫰", "🤟", "🤘", "🤙", "🫵", "🫱", "🫲", "🫸", "🫷", "🫳", "🫴", "👈", "👉", "👆", "🖕", "👇", "☝️", "👍", "👎", "✊", "👊", "🤛", "🤜", "👋🏻", "🤚🏻", "🖐🏻", "✋🏻", "🖖🏻", "👌🏻", "🤌🏻", "🤏🏻", "✌🏻", "🤞🏻", "🫰🏻", "🤟🏻", "🤘🏻", "🤙🏻", "🫵🏻", "🫱🏻", "🫲🏻", "🫸🏻", "🫷🏻", "🫳🏻", "🫴🏻", "👈🏻", "👉🏻", "👆🏻", "🖕🏻", "👇🏻", "☝🏻", "👍🏻", "👎🏻", "✊🏻", "👊🏻", "🤛🏻", "🤜🏻", "👋🏼", "🤚🏼", "🖐🏼", "✋🏼", "🖖🏼", "👌🏼", "🤌🏼", "🤏🏼", "✌🏼", "🤞🏼", "🫰🏼", "🤟🏼", "🤘🏼", "🤙🏼", "🫵🏼", "🫱🏼", "🫲🏼", "🫸🏼", "🫷🏼", "🫳🏼", "🫴🏼", "👈🏼", "👉🏼", "👆🏼", "🖕🏼", "👇🏼", "☝🏼", "👍🏼", "👎🏼", "✊🏼", "👊🏼", "🤛🏼", "🤜🏼", "👋🏽", "🤚🏽", "🖐🏽", "✋🏽", "🖖🏽", "👌🏽", "🤌🏽", "🤏🏽", "✌🏽", "🤞🏽", "🫰🏽", "🤟🏽", "🤘🏽", "🤙🏽", "🫵🏽", "🫱🏽", "🫲🏽", "🫸🏽", "🫷🏽", "🫳🏽", "🫴🏽", "👈🏽", "👉🏽", "👆🏽", "🖕🏽", "👇🏽", "☝🏽", "👍🏽", "👎🏽", "✊🏽", "👊🏽", "🤛🏽", "🤜🏽", "👋🏾", "🤚🏾", "🖐🏾", "✋🏾", "🖖🏾", "👌🏾", "🤌🏾", "🤏🏾", "✌🏾", "🤞🏾", "🫰🏾", "🤟🏾", "🤘🏾", "🤙🏾", "🫵🏾", "🫱🏾", "🫲🏾", "🫸🏾", "🫷🏾", "🫳🏾", "🫴🏾", "👈🏾", "👉🏾", "👆🏾", "🖕🏾", "👇🏾", "☝🏾", "👍🏾", "👎🏾", "✊🏾", "👊🏾", "🤛🏾", "🤜🏾", "👋🏿", "🤚🏿", "🖐🏿", "✋🏿", "🖖🏿", "👌🏿", "🤌🏿", "🤏🏿", "✌🏿", "🤞🏿", "🫰🏿", "🤟🏿", "🤘🏿", "🤙🏿", "🫵🏿", "🫱🏿", "🫲🏿", "🫸🏿", "🫷🏿", "🫳🏿", "🫴🏿", "👈🏿", "👉🏿", "👆🏿", "🖕🏿", "👇🏿", "☝🏿", "👍🏿", "👎🏿", "✊🏿", "👊🏿", "🤛🏿", "🤜🏿"
                ],
                [
                    "🥼", "🦺", "👔", "👕", "🧥", "👗", "👘", "🥻", "🩱", "👙", "👚", "👛"
                ],
                [
                    "👋", "🤚", "🖐", "✋", "🖖", "👌", "🤌", "🤏", "✌️", "🤞", "🫰", "🤟", "🤘", "🤙", "🫵", "🫱", "🫲", "🫸", "🫷", "🫳", "🫴", "👈", "👉", "👆", "🖕", "👇", "☝️", "👍", "👎", "✊", "👊", "🤛", "🤜", "👋🏻", "🤚🏻", "🖐🏻", "✋🏻", "🖖🏻", "👌🏻", "🤌🏻", "🤏🏻", "✌🏻", "🤞🏻", "🫰🏻", "🤟🏻", "🤘🏻", "🤙🏻", "🫵🏻", "🫱🏻", "🫲🏻", "🫸🏻", "🫷🏻", "🫳🏻", "🫴🏻", "👈🏻", "👉🏻", "👆🏻", "🖕🏻", "👇🏻", "☝🏻", "👍🏻", "👎🏻", "✊🏻", "👊🏻", "🤛🏻", "🤜🏻", "👋🏼", "🤚🏼", "🖐🏼", "✋🏼", "🖖🏼", "👌🏼", "🤌🏼", "🤏🏼", "✌🏼", "🤞🏼", "🫰🏼", "🤟🏼", "🤘🏼", "🤙🏼", "🫵🏼", "🫱🏼", "🫲🏼", "🫸🏼", "🫷🏼", "🫳🏼", "🫴🏼", "👈🏼", "👉🏼", "👆🏼", "🖕🏼", "👇🏼", "☝🏼", "👍🏼", "👎🏼", "✊🏼", "👊🏼", "🤛🏼", "🤜🏼", "👋🏽", "🤚🏽", "🖐🏽", "✋🏽", "🖖🏽", "👌🏽", "🤌🏽", "🤏🏽", "✌🏽", "🤞🏽", "🫰🏽", "🤟🏽", "🤘🏽", "🤙🏽", "🫵🏽", "🫱🏽", "🫲🏽", "🫸🏽", "🫷🏽", "🫳🏽", "🫴🏽", "👈🏽", "👉🏽", "👆🏽", "🖕🏽", "👇🏽", "☝🏽", "👍🏽", "👎🏽", "✊🏽", "👊🏽", "🤛🏽", "🤜🏽", "👋🏾", "🤚🏾", "🖐🏾", "✋🏾", "🖖🏾", "👌🏾", "🤌🏾", "🤏🏾", "✌🏾", "🤞🏾", "🫰🏾", "🤟🏾", "🤘🏾", "🤙🏾", "🫵🏾", "🫱🏾", "🫲🏾", "🫸🏾", "🫷🏾", "🫳🏾", "🫴🏾", "👈🏾", "👉🏾", "👆🏾", "🖕🏾", "👇🏾", "☝🏾", "👍🏾", "👎🏾", "✊🏾", "👊🏾", "🤛🏾", "🤜🏾", "👋🏿", "🤚🏿", "🖐🏿", "✋🏿", "🖖🏿", "👌🏿", "🤌🏿", "🤏🏿", "✌🏿", "🤞🏿", "🫰🏿", "🤟🏿", "🤘🏿", "🤙🏿", "🫵🏿", "🫱🏿", "🫲🏿", "🫸🏿", "🫷🏿", "🫳🏿", "🫴🏿", "👈🏿", "👉🏿", "👆🏿", "🖕🏿", "👇🏿", "☝🏿", "👍🏿", "👎🏿", "✊🏿", "👊🏿", "🤛🏿", "🤜🏿"
                ],
                [
                    "👖", "🩲", "🩳"
                ],
                [
                    "👞", "👟", "🥾", "🥿", "👠", "👡", "🩰", "👢"
                ],
                [
                    "👞", "👟", "🥾", "🥿", "👠", "👡", "🩰", "👢"
                ],
                [
                    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲", "🥹", "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸", "🥳", "😏", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣", "😖", "😫", "😩", "🥺", "😢", "😭", "😮‍💨", "😤", "😠", "😡", "🤬", "🤯", "😳", "🥵", "🥶", "😱", "😨", "😰", "😥", "😓", "🫣", "🤗", "🫡", "🤔", "🫢", "🤭", "🤫", "🤥", "😶", "😶‍🌫️", "😐", "😑", "😬", "🫨", "🫠", "🙄", "😯", "😦", "😧", "😮", "😲", "🥱", "😴", "🤤", "😪", "😵", "😵‍💫", "🫥", "🤐", "🥴", "🤢", "🤮", "🤧", "😷", "🤒", "🤕", "🤑", "🤠", "😈", "👿", "👹", "👺", "🤡", "💩", "👻", "💀", "☠️", "👽", "👾", "🎃", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾", "👶", "👧", "🧒", "👦", "👩", "🧑", "👨", "👩‍🦱", "🧑‍🦱", "👨‍🦱", "👩‍🦰", "🧑‍🦰", "👨‍🦰", "👱‍♀️", "👱", "👱‍♂️", "👩‍🦳", "🧑‍🦳", "👨‍🦳", "👩‍🦲", "🧑", "👨‍🦲", "🧔‍♀️", "🧔", "🧔‍♂️", "👵", "🧓", "👴", "👲", "👳‍♀️", "👳", "👳‍♂️", "🧕", "👮‍♀️", "👮", "👮‍♂️", "👷‍♀️", "👷", "👷‍♂️", "💂‍♀️", "💂", "💂‍♂️", "🕵️‍♀️", "🕵️", "🕵️‍♂️", "👩‍⚕️", "🧑‍⚕️", "👨‍⚕️", "👩‍🌾", "🧑‍🌾", "👨", "👩‍🍳", "🧑‍🍳", "👨‍🍳", "👩‍🎓", "🧑‍🎓", "👨‍🎓", "👩‍🎤", "🧑‍🎤", "👨‍🎤", "👩‍🏫", "🧑‍🏫", "👨‍🏫", "👩‍🏭", "🧑‍🏭", "👨‍🏭", "👩‍💻", "🧑‍💻", "👨‍💻", "👩‍💼", "🧑‍💼", "👨‍💼", "👩‍🔧", "🧑‍🔧", "👨‍🔧", "👩", "🧑‍🔬", "👨‍🔬", "👩‍🎨", "🧑‍🎨", "👨‍🎨", "👩‍🚒", "🧑‍🚒", "👨‍🚒", "👩‍✈️", "🧑‍✈️", "👨‍✈️", "👩‍🚀", "🧑‍🚀", "👨‍🚀", "👩‍⚖️", "🧑‍⚖️", "👨‍⚖️", "👰‍♀️", "👰", "👰‍♂️", "🤵‍♀️", "🤵", "🤵‍♂️", "👸", "🫅", "🤴", "🥷", "🦸‍♀️", "🦸", "🦸‍♂️", "🦹‍♀️", "🦹", "🦹‍♂️", "🤶", "🧑‍🎄", "🎅", "🧙‍♀️", "🧙", "🧙‍♂️", "🧝‍♀️", "🧝", "🧝‍♂️", "🧛‍♀️", "🧛", "🧛‍♂️", "🧟‍♀️", "🧟", "🧟‍♂️", "👼", "🙎‍♀️", "🙎", "🙎‍♂️", "🙍‍♀️", "🙍", "🙍‍♂️", "💇‍♀️", "💇", "💇‍♂️", "💆‍♀️", "💆", "💆‍♂️", "🧖‍♀️", "🧖", "🧖‍♂️", "👶🏻", "👧🏻", "🧒🏻", "👦🏻", "👩🏻", "🧑🏻", "👨🏻", "👩🏻‍🦱", "🧑🏻‍🦱", "👨🏻‍🦱", "👩🏻‍🦰", "🧑🏻‍🦰", "👨🏻‍🦰", "👱🏻‍♀️", "👱🏻", "👱🏻‍♂️", "👩🏻‍🦳", "🧑🏻‍🦳", "👨🏻‍🦳", "👩🏻‍🦲", "🧑🏻‍🦲", "👨🏻", "🧔🏻‍♀️", "🧔🏻", "🧔🏻‍♂️", "👵🏻", "🧓🏻", "👴🏻", "👲🏻", "👳🏻‍♀️", "👳🏻", "👳🏻‍♂️", "🧕🏻", "👮🏻‍♀️", "👮🏻", "👮🏻‍♂️", "👷🏻‍♀️", "👷🏻", "👷🏻‍♂️", "💂🏻‍♀️", "💂🏻", "💂🏻‍♂️", "🕵🏻‍♀️", "🕵🏻", "🕵🏻‍♂️", "👩🏻‍⚕️", "🧑🏻‍⚕️", "👨🏻‍⚕️", "👩🏻‍🌾", "🧑🏻‍🌾", "👨🏻‍🌾", "👩🏻‍🍳", "🧑🏻‍🍳", "👨🏻‍🍳", "👩🏻‍🎓", "🧑🏻‍🎓", "👨🏻‍🎓", "🧑🏻‍🎤", "👨🏻‍🎤", "👩🏻‍🏫", "🧑🏻‍🏫", "👨🏻‍🏫", "🧑🏻‍🏭", "👨🏻‍🏭", "👩🏻‍💻", "🧑🏻‍💻", "👨🏻‍💻", "👩🏻‍💼", "🧑🏻‍💼", "👨🏻‍💼", "👩🏻‍🔧", "🧑🏻‍🔧", "👨🏻‍🔧", "👩🏻‍🔬", "🧑🏻‍🔬", "👨🏻‍🔬", "👩🏻‍🎨", "🧑🏻‍🎨", "👨🏻‍🎨", "👩🏻‍🚒", "👨🏻‍🚒", "👩🏻‍✈️", "🧑🏻‍✈️", "👨🏻‍✈️", "👩🏻‍🚀", "👨🏻‍🚀", "👩🏻‍⚖️", "🧑🏻‍⚖️", "👨🏻‍⚖️", "👰🏻‍♀️", "👰🏻", "👰🏻‍♂️", "🤵🏻‍♀️", "🤵🏻", "🤵🏻‍♂️", "👸🏻", "🫅🏻", "🤴🏻", "🥷🏻", "🦸🏻", "🦸🏻‍♂️", "🦹🏻‍♀️", "🦹🏻", "🦹🏻‍♂️", "🤶🏻", "🧑🏻‍🎄", "🎅🏻", "🧙🏻‍♀️", "🧙🏻", "🧙🏻‍♂️", "🧝🏻‍♀️", "🧝🏻", "🧝🏻‍♂️", "🧛🏻‍♀️", "🧛🏻", "🧛🏻‍♂️", "💁🏻‍♀️", "💁🏻", "💁🏻‍♂️", "🙅🏻‍♀️", "🙅🏻", "🙅🏻‍♂️", "🙆🏻‍♀️", "🙆🏻", "🙆🏻‍♂️", "🙋🏻‍♀️", "🙋🏻", "🙋🏻‍♂️", "🧏🏻‍♀️", "🧏🏻", "🤦🏻‍♀️", "🤦🏻", "🤦🏻‍♂️", "🤷🏻‍♀️", "🤷🏻", "🤷🏻‍♂️", "🙎🏻", "🙎🏻‍♂️", "🙍🏻‍♀️", "🙍🏻", "🙍🏻‍♂️", "💇🏻‍♀️", "💇", "💇🏻‍♂️", "💆🏻‍♀️", "💆🏻", "💆🏻‍♂️", "🧖🏻‍♀️", "🧖🏻", "🧖🏻‍♂️", "👶🏼", "👧🏼", "🧒🏼", "👦🏼", "👩🏼", "🧑🏼", "👨🏼", "👩🏼‍🦱", "🧑🏼‍🦱", "👨🏼‍🦱", "👩🏼‍🦰", "🧑🏼‍🦰", "👨🏼‍🦰", "👱🏼‍♀️", "👱🏼", "👱🏼‍♂️", "👩🏼‍🦳", "🧑🏼‍🦳", "👨🏼‍🦳", "👩🏼‍🦲", "🧑🏼‍🦲", "👨🏼", "🧔🏼‍♀️", "🧔🏼", "🧔🏼‍♂️", "👵🏼", "🧓🏼", "👴🏼", "👲🏼", "👳🏼‍♀️", "👳🏼", "👳🏼‍♂️", "🧕🏼", "👮🏼‍♀️", "👮🏼", "👮🏼‍♂️", "👷🏼‍♀️", "👷🏼", "👷🏼‍♂️", "💂🏼‍♀️", "💂🏼", "💂🏼‍♂️", "🕵🏼‍♀️", "🕵🏼", "🕵🏼‍♂️", "👩🏼‍⚕️", "🧑🏼‍⚕️", "👨🏼‍⚕️", "👩🏼‍🌾", "🧑🏼‍🌾", "👨🏼‍🌾", "👩🏼‍🍳", "🧑🏼‍🍳", "👨🏼‍🍳", "👩🏼‍🎓", "🧑🏼‍🎓", "👨🏼‍🎓", "🧑🏼‍🎤", "👨🏼‍🎤", "👩🏼‍🏫", "🧑🏼‍🏫", "👨🏼‍🏫", "🧑🏼‍🏭", "👨🏼‍🏭", "👩🏼‍💻", "🧑🏼‍💻", "👨🏼‍💻", "👩🏼‍💼", "🧑🏼‍💼", "👨🏼‍💼", "👩🏼‍🔧", "🧑🏼‍🔧", "👨🏼‍🔧", "👩🏼‍🔬", "🧑🏼‍🔬", "👨🏼‍🔬", "👩🏼‍🎨", "🧑🏼‍🎨", "👨🏼‍🎨", "👩🏼‍🚒", "👨🏼‍🚒", "👩🏼‍✈️", "🧑🏼‍✈️", "👨🏼‍✈️", "👩🏼‍🚀", "👨🏼‍🚀", "👩🏼‍⚖️", "🧑🏼‍⚖️", "👨🏼‍⚖️", "👰🏼‍♀️", "👰🏼", "👰🏼‍♂️", "🤵🏼‍♀️", "🤵🏼", "🤵🏼‍♂️", "👸🏼", "🫅🏼", "🤴🏼", "🥷🏼", "🦸🏼", "🦸🏼‍♂️", "🦹🏼‍♀️", "🦹🏼", "🦹🏼‍♂️", "🤶🏼", "🧑🏼‍🎄", "🎅🏼", "🧙🏼‍♀️", "🧙🏼", "🧙🏼‍♂️", "🧝🏼‍♀️", "🧝🏼", "🧝🏼‍♂️", "🧛🏼‍♀️", "🧛🏼", "🧛🏼‍♂️", "🙇🏼‍♀️", "🙇🏼", "🙇🏼‍♂️", "💁🏼‍♀️", "💁🏼", "💁🏼‍♂️", "🙅🏼‍♀️", "🙅🏼", "🙅🏼‍♂️", "🙆🏼‍♀️", "🙆🏼", "🙆🏼‍♂️", "🙋🏼‍♀️", "🙋🏼", "🧏🏼‍♀️", "🧏🏼", "🧏🏼‍♂️", "🤦🏼‍♀️", "🤦🏼", "🤦🏼‍♂️", "🤷🏼", "🤷🏼‍♂️", "🙎🏼‍♀️", "🙎🏼", "🙎🏼‍♂️", "🙍🏼‍♀️", "🙍🏼‍♂️", "💇🏼‍♀️", "💇🏼", "💇🏼‍♂️", "💆🏼‍♀️", "💆🏼", "💆🏼‍♂️", "🧖🏼‍♀️", "🧖🏼", "🧖🏼‍♂️", "👶🏽", "👧🏽", "🧒🏽", "👦🏽", "👩🏽", "🧑🏽", "👨🏽", "👩🏽‍🦱", "🧑🏽‍🦱", "👨🏽‍🦱", "👩🏽‍🦰", "🧑🏽‍🦰", "👨🏽‍🦰", "👱🏽‍♀️", "👱🏽", "👱🏽‍♂️", "👩🏽‍🦳", "🧑🏽‍🦳", "👨🏽‍🦳", "👩🏽‍🦲", "🧑🏽‍🦲", "👨🏽", "🧔🏽‍♀️", "🧔🏽", "🧔🏽‍♂️", "👵🏽", "🧓🏽", "👴🏽", "👲🏽", "👳🏽‍♀️", "👳🏽", "👳🏽‍♂️", "🧕🏽", "👮🏽‍♀️", "👮🏽", "👮🏽‍♂️", "👷🏽‍♀️", "👷🏽", "👷🏽‍♂️", "💂🏽‍♀️", "💂🏽", "💂🏽‍♂️", "🕵🏽‍♀️", "🕵🏽", "🕵🏽‍♂️", "👩🏽‍⚕️", "🧑🏽‍⚕️", "👨🏽‍⚕️", "👩🏽‍🌾", "🧑🏽‍🌾", "👨🏽‍🌾", "👩🏽‍🍳", "🧑🏽‍🍳", "👨🏽‍🍳", "👩🏽‍🎓", "🧑🏽‍🎓", "👨🏽‍🎓", "🧑🏽‍🎤", "👨🏽‍🎤", "👩🏽‍🏫", "🧑🏽‍🏫", "👨🏽‍🏫", "🧑🏽‍🏭", "👨🏽‍🏭", "👩🏽‍💻", "🧑🏽‍💻", "👨🏽‍💻", "👩🏽‍💼", "🧑🏽‍💼", "👨🏽‍💼", "👩🏽‍🔧", "🧑🏽‍🔧", "👨🏽‍🔧", "👩🏽‍🔬", "🧑🏽‍🔬", "👨🏽‍🔬", "👩🏽‍🎨", "🧑🏽‍🎨", "👨🏽‍🎨", "👩🏽‍🚒", "👨🏽‍🚒", "👩🏽‍✈️", "🧑🏽‍✈️", "👨🏽‍✈️", "👩🏽‍🚀", "👨🏽‍🚀", "👩🏽‍⚖️", "🧑🏽‍⚖️", "👨🏽‍⚖️", "👰🏽‍♀️", "👰🏽", "👰🏽‍♂️", "🤵🏽‍♀️", "🤵🏽", "🤵🏽‍♂️", "👸🏽", "🫅🏽", "🤴🏽", "🥷🏽", "🦸🏽", "🦸🏽‍♂️", "🦹🏽‍♀️", "🦹🏽", "🦹🏽‍♂️", "🤶🏽", "🧑🏽‍🎄", "🎅🏽", "🧙🏽‍♀️", "🧙🏽", "🧙🏽‍♂️", "🧝🏽‍♀️", "🧝🏽", "🧝🏽‍♂️", "🧛🏽‍♀️", "🧛🏽", "🧛🏽‍♂️", "🧜🏽‍♀️", "🧜🏽", "🧜🏽‍♂️", "🧚🏽‍♀️", "🧚🏽", "🧚🏽‍♂️", "👼🏽", "🤰🏽", "🫄🏽", "🫃🏽", "🤱🏽", "👩🏽‍🍼", "👨🏽‍🍼", "🙇🏽‍♀️", "🙇🏽", "🙇🏽‍♂️", "💁🏽‍♀️", "💁🏽", "🙅🏽‍♀️", "🙅🏽", "🙅🏽‍♂️", "🙆🏽‍♀️", "🙆🏽", "🙆🏽‍♂️", "🙋🏽", "🙋🏽‍♂️", "🧏🏽‍♀️", "🧏🏽", "🧏🏽‍♂️", "🤦🏽‍♀️", "🤦🏽‍♂️", "🤷🏽‍♀️", "🤷🏽", "🤷🏽‍♂️", "🙎🏽‍♀️", "🙎🏽", "🙎🏽‍♂️", "🙍🏽‍♀️", "🙍🏽", "🙍🏽‍♂️", "💇🏽‍♀️", "💇🏽", "💇🏽‍♂️", "💆🏽‍♀️", "💆🏽", "💆🏽‍♂️", "🧖🏽‍♀️", "🧖🏽", "🧖🏽‍♂️", "👶🏾", "👧🏾", "🧒🏾", "👦🏾", "👩🏾", "🧑🏾", "👨🏾", "👩🏾‍🦱", "🧑🏾‍🦱", "👨🏾‍🦱", "👩🏾‍🦰", "🧑🏾‍🦰", "👨🏾‍🦰", "👱🏾‍♀️", "👱🏾", "👱🏾‍♂️", "👩🏾‍🦳", "🧑🏾‍🦳", "👨🏾‍🦳", "👩🏾‍🦲", "🧑🏾‍🦲", "👨🏾", "🧔🏾‍♀️", "🧔🏾", "🧔🏾‍♂️", "👵🏾", "🧓🏾", "👴🏾", "👲🏾", "👳🏾‍♀️", "👳🏾", "👳🏾‍♂️", "🧕🏾", "👮🏾‍♀️", "👮🏾", "👮🏾‍♂️", "👷🏾‍♀️", "👷🏾", "👷🏾‍♂️", "💂🏾‍♀️", "💂🏾", "💂🏾‍♂️", "🕵🏾‍♀️", "🕵🏾", "🕵🏾‍♂️", "👩🏾‍⚕️", "🧑🏾‍⚕️", "👨🏾‍⚕️", "👩🏾‍🌾", "🧑🏾‍🌾", "👨🏾‍🌾", "👩🏾‍🍳", "🧑🏾‍🍳", "👨🏾‍🍳", "👩🏾‍🎓", "🧑🏾‍🎓", "👨🏾‍🎓", "🧑🏾‍🎤", "👨🏾‍🎤", "👩🏾‍🏫", "🧑🏾‍🏫", "👨🏾‍🏫", "🧑🏾‍🏭", "👨🏾‍🏭", "👩🏾‍💻", "🧑🏾‍💻", "👨🏾‍💻", "👩🏾‍💼", "🧑🏾‍💼", "👨🏾‍💼", "👩🏾‍🔧", "🧑🏾‍🔧", "👨🏾‍🔧", "👩🏾‍🔬", "🧑🏾‍🔬", "👨🏾‍🔬", "👩🏾‍🎨", "🧑🏾‍🎨", "👨🏾‍🎨", "👩🏾‍🚒", "👨🏾‍🚒", "👩🏾‍✈️", "🧑🏾‍✈️", "👨🏾‍✈️", "👩🏾‍🚀", "👨🏾‍🚀", "👩🏾‍⚖️", "🧑🏾‍⚖️", "👨🏾‍⚖️", "👰🏾‍♀️", "👰🏾", "👰🏾‍♂️", "🤵🏾‍♀️", "🤵🏾", "🤵🏾‍♂️", "👸🏾", "🫅🏾", "🤴🏾", "🥷🏾", "🦸🏾", "🦸🏾‍♂️", "🦹🏾‍♀️", "🦹🏾", "🦹🏾‍♂️", "🤶🏾", "🧑🏾‍🎄", "🎅🏾", "🧙🏾‍♀️", "🧙🏾", "🧙🏾‍♂️", "🧝🏾‍♀️", "🧝🏾", "🧝🏾‍♂️", "🧛🏾‍♀️", "🧛🏾", "🧛🏾‍♂️", "🧜🏾‍♀️", "🧜🏾", "🧜🏾‍♂️", "🧚🏾‍♀️", "🧚🏾", "🧚🏾‍♂️", "👼🏾", "🤰🏾", "🫄🏾", "🫃🏾", "🤱🏾", "👩🏾‍🍼", "👨🏾‍🍼", "🙇🏾‍♀️", "🙇🏾", "🙇🏾‍♂️", "💁🏾‍♀️", "💁🏾", "🙅🏾‍♀️", "🙅🏾", "🙅🏾‍♂️", "🙆🏾‍♀️", "🙆🏾", "🙆🏾‍♂️", "🙋🏾", "🙋🏾‍♂️", "🧏🏾‍♀️", "🧏🏾", "🧏🏾‍♂️", "🤦🏾‍♀️", "🤦🏾‍♂️", "🤷🏾‍♀️", "🤷🏾", "🤷🏾‍♂️", "🙎🏾‍♀️", "🙎🏾", "🙎🏾‍♂️", "🙍🏾‍♀️", "🙍🏾", "🙍🏾‍♂️", "💇🏾‍♀️", "💇🏾", "💇🏾‍♂️", "💆🏾‍♀️", "💆🏾", "💆🏾‍♂️", "🧖🏾‍♀️", "🧖🏾", "🧖🏾‍♂️", "👶🏿", "👧🏿", "🧒🏿", "👦🏿", "👩🏿", "🧑🏿", "👨🏿", "👩🏿‍🦱", "🧑🏿", "👨🏿‍🦱", "👩🏿‍🦰", "🧑🏿‍🦰", "👨🏿‍🦰", "👱🏿‍♀️", "👱🏿", "👩🏿‍🦳", "🧑🏿‍🦳", "👨🏿‍🦳", "👩🏿‍🦲", "🧑🏿‍🦲", "👨🏿‍🦲", "🧔🏿‍♀️", "🧔🏿", "🧔🏿‍♂️", "👵🏿", "🧓🏿", "👴🏿", "👲🏿", "👳🏿‍♀️", "👳🏿", "👳🏿‍♂️", "🧕🏿", "👮🏿‍♀️", "👮🏿", "👮🏿‍♂️", "👷🏿‍♀️", "👷🏿‍♂️", "💂🏿‍♀️", "💂🏿", "💂🏿‍♂️", "🕵🏿‍♀️", "🕵🏿", "🕵🏿‍♂️", "👩🏿‍⚕️", "🧑🏿‍⚕️", "👨🏿‍⚕️", "👩🏿‍🌾", "🧑🏿‍🌾", "👨🏿", "👩🏿‍🍳", "🧑🏿‍🍳", "👨🏿‍🍳", "👩🏿‍🎓", "🧑🏿‍🎓", "👨🏿‍🎓", "👩🏿‍🎤", "🧑🏿‍🎤", "👨🏿‍🎤", "👩🏿‍🏫", "🧑🏿‍🏫", "👨🏿‍🏫", "👩🏿‍🏭", "🧑🏿‍🏭", "👨🏿‍🏭", "👩🏿‍💻", "🧑🏿‍💻", "👨🏿‍💻", "👩🏿‍💼", "🧑🏿‍💼", "👨🏿‍💼", "👩🏿‍🔧", "🧑🏿‍🔧", "👨🏿‍🔧", "👩🏿", "🧑🏿‍🔬", "👨🏿‍🔬", "👩🏿‍🎨", "🧑🏿‍🎨", "👨🏿‍🎨", "👩🏿‍🚒", "🧑🏿‍🚒", "👨🏿‍🚒", "👩🏿‍✈️", "🧑🏿‍✈️", "👨🏿‍✈️", "👩🏿‍🚀", "🧑🏿‍🚀", "👨🏿‍🚀", "👩🏿‍⚖️", "🧑🏿‍⚖️", "👨🏿‍⚖️", "👰🏿‍♀️", "👰🏿", "👰🏿‍♂️", "🤵🏿‍♀️", "🤵🏿", "🤵🏿‍♂️", "👸🏿", "🫅🏿", "🤴🏿", "🥷🏿", "🦸🏿‍♀️", "🦸🏿", "🦸🏿‍♂️", "🦹🏿‍♀️", "🦹🏿", "🦹🏿‍♂️", "🤶🏿", "🎅🏿", "🧙🏿‍♀️", "🧙🏿", "🧙🏿‍♂️", "🧝🏿‍♀️", "🧝🏿", "🧝🏿‍♂️", "🧛🏿‍♀️", "🧛🏿", "🧛🏿‍♂️", "🧜🏿‍♀️", "🧜🏿", "🧜🏿‍♂️", "🧚🏿‍♀️", "🧚🏿", "🧚🏿‍♂️", "👼🏿", "🤰🏿", "🫄🏿", "🫃🏿", "🤱🏿", "👩🏿‍🍼", "🧑🏿‍🍼", "👨🏿‍🍼", "🙇🏿‍♀️", "🙇🏿", "🙇🏿‍♂️", "💁🏿‍♀️", "💁🏿", "💁🏿‍♂️", "🙅🏿‍♀️", "🙅🏿", "🙅🏿‍♂️", "🙆🏿‍♀️", "🙆🏿", "🙆🏿‍♂️", "🙋🏿‍♀️", "🙋🏿", "🙋🏿‍♂️", "🧏🏿‍♀️", "🧏🏿", "🧏🏿‍♂️", "🤦🏿‍♀️", "🤦🏿", "🤦🏿‍♂️", "🤷🏿‍♀️", "🤷🏿", "🤷🏿‍♂️", "🙎🏿‍♀️", "🙎🏿", "🙎🏿‍♂️", "🙍🏿‍♀️", "🙍🏿", "🙍🏿‍♂️", "💇🏿‍♀️", "💇🏿", "💇🏿‍♂️", "💆🏿‍♀️", "💆🏿", "💆🏿‍♂️", "🧖🏿‍♀️", "🧖🏿", "🧖🏿‍♂️", "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐻‍❄️", "🐨", "🐯", "🦁", "🐮", "🐷", "🐽", "🐸", "🐵", "🙈", "🙉", "🙊", "🐔", "🐧", "🐦", "🐦‍⬛", "🐤", "🐣", "🐥", "🦆", "🦅", "🦉", "🦇", "🐺", "🐗", "🐴", "🦄", "🐝", "👋", "🤚", "🖐", "✋", "🖖", "👌", "🤌", "🤏", "✌️", "🤞", "🫰", "🤟", "🤘", "🤙", "🫵", "🫱", "🫲", "🫸", "🫷", "🫳", "🫴", "👈", "👉", "👆", "🖕", "👇", "☝️", "👍", "👎", "✊", "👊", "🤛", "🤜", "👋🏻", "🤚🏻", "🖐🏻", "✋🏻", "🖖🏻", "👌🏻", "🤌🏻", "🤏🏻", "✌🏻", "🤞🏻", "🫰🏻", "🤟🏻", "🤘🏻", "🤙🏻", "🫵🏻", "🫱🏻", "🫲🏻", "🫸🏻", "🫷🏻", "🫳🏻", "🫴🏻", "👈🏻", "👉🏻", "👆🏻", "🖕🏻", "👇🏻", "☝🏻", "👍🏻", "👎🏻", "✊🏻", "👊🏻", "🤛🏻", "🤜🏻", "👋🏼", "🤚🏼", "🖐🏼", "✋🏼", "🖖🏼", "👌🏼", "🤌🏼", "🤏🏼", "✌🏼", "🤞🏼", "🫰🏼", "🤟🏼", "🤘🏼", "🤙🏼", "🫵🏼", "🫱🏼", "🫲🏼", "🫸🏼", "🫷🏼", "🫳🏼", "🫴🏼", "👈🏼", "👉🏼", "👆🏼", "🖕🏼", "👇🏼", "☝🏼", "👍🏼", "👎🏼", "✊🏼", "👊🏼", "🤛🏼", "🤜🏼", "👋🏽", "🤚🏽", "🖐🏽", "✋🏽", "🖖🏽", "👌🏽", "🤌🏽", "🤏🏽", "✌🏽", "🤞🏽", "🫰🏽", "🤟🏽", "🤘🏽", "🤙🏽", "🫵🏽", "🫱🏽", "🫲🏽", "🫸🏽", "🫷🏽", "🫳🏽", "🫴🏽", "👈🏽", "👉🏽", "👆🏽", "🖕🏽", "👇🏽", "☝🏽", "👍🏽", "👎🏽", "✊🏽", "👊🏽", "🤛🏽", "🤜🏽", "👋🏾", "🤚🏾", "🖐🏾", "✋🏾", "🖖🏾", "👌🏾", "🤌🏾", "🤏🏾", "✌🏾", "🤞🏾", "🫰🏾", "🤟🏾", "🤘🏾", "🤙🏾", "🫵🏾", "🫱🏾", "🫲🏾", "🫸🏾", "🫷🏾", "🫳🏾", "🫴🏾", "👈🏾", "👉🏾", "👆🏾", "🖕🏾", "👇🏾", "☝🏾", "👍🏾", "👎🏾", "✊🏾", "👊🏾", "🤛🏾", "🤜🏾", "👋🏿", "🤚🏿", "🖐🏿", "✋🏿", "🖖🏿", "👌🏿", "🤌🏿", "🤏🏿", "✌🏿", "🤞🏿", "🫰🏿", "🤟🏿", "🤘🏿", "🤙🏿", "🫵🏿", "🫱🏿", "🫲🏿", "🫸🏿", "🫷🏿", "🫳🏿", "🫴🏿", "👈🏿", "👉🏿", "👆🏿", "🖕🏿", "👇🏿", "☝🏿", "👍🏿", "👎🏿", "✊🏿", "👊🏿", "🤛🏿", "🤜🏿", "🥼", "🦺", "👔", "👕", "🧥", "👗", "👘", "🥻", "🩱", "👙", "👚", "👛", "👖", "🩲", "🩳", "👞", "👟", "🥾", "🥿", "👠", "👡", "🩰", "👢"
                ]
            ],
            emojis_item: [
                "⌚️", "📱", "📲", "💻", "⌨️", "🖥", "🖨", "🖱", "🖲", "🕹", "🗜", "💽", "💾", "💿", "📀", "📼", "📷", "📸", "📹", "🎥", "📽", "🎞", "📞", "☎️", "📟", "📠", "📺", "📻", "🎙", "🎚", "🎛", "🧭", "⏱", "⏲", "⏰", "🕰", "⌛️", "⏳", "📡", "🔋", "🪫", "🔌", "💡", "🔦", "🕯", "🪔", "🧯", "🛢", "🛍️", "💸", "💵", "💴", "💶", "💷", "🪙", "💰", "💳", "💎", "⚖️", "🪮", "🪜", "🧰", "🪛", "🔧", "🔨", "⚒", "🛠", "⛏", "🔩", "⚙️", "🪤", "🧱", "⛓", "🧲", "🔫", "💣", "🧨", "🪓", "🔪", "🗡", "⚔️", "🛡", "🚬", "⚰️", "⚱️", "🏺", "🔮", "📿", "🧿", "🪬", "💈", "⚗️", "🔭", "🔬", "🕳", "🩹", "🩺", "🩻", "🩼", "💊", "💉", "🩸", "🧬", "🦠", "🧫", "🧪", "🌡", "🧹", "🪠", "🧺", "🧻", "🚽", "🚰", "🚿", "🛁", "🛀", "🧼", "🪥", "🪒", "🧽", "🪣", "🧴", "🛎", "🔑", "🗝", "🚪", "🪑", "🛋", "🛏", "🛌", "🧸", "🪆", "🖼", "🪟", "🛍", "🛒", "🎁", "🎈", "🎏", "🎀", "🪄", "🪅", "🎊", "🎉", "🪩", "🎎", "🏮", "🎐", "🧧", "✉️", "📩", "📨", "📧", "💌", "📥", "📤", "📦", "🏷", "🪧", "📪", "📫", "📬", "📭", "📮", "📯", "📜", "📃", "📄", "📑", "🧾", "📊", "📈", "📉", "🗒", "🗓", "📆", "📅", "🗑", "🪪", "📇", "🗃", "🗳", "📋", "📁", "📂", "🗂", "🗞", "📰", "📓", "📔", "📒", "📕", "📗", "📘", "📙", "📚", "📖", "🔖", "🧷", "🔗", "📎", "🖇", "📐", "📏", "🧮", "📌", "📍", "✂️", "🖊", "🖋", "✒️", "🖌", "🖍", "📝", "✏️", "🔍", "🔎", "🔏", "🔐", "🔒", "🔓", "🚗", "🚕", "🚙", "🚌", "🚎", "🏎", "🚓", "🚑", "🚒", "🚐", "🛻", "🚚", "🚛", "🚜", "🦯", "🦽", "🦼", "🛴", "🚲", "🛵", "🏍", "🛺", "🚨", "🚔", "🚍", "🚘", "🚖", "🛞", "🚡", "🚠", "🚟", "🚃", "🚋", "🚝", "🚄", "🚅", "🚈", "🚂", "🚆", "🚇", "🚊", "🚉", "✈️", "🛫", "🛬", "🛩", "💺", "🛰", "🚀", "🛸", "🚁", "🛶", "⛵️", "🚤", "🛥", "🛳", "⛴", "🚢", "⚓️", "🛟", "🪝", "⛽️", "🚧", "🚦", "🚥", "🚏", "🗺", "🗿", "🗽", "🗼", "🏰", "🏯", "🏟", "🎡", "🎢", "🛝", "🎠", "⛲️", "⛱", "🏖", "🏝", "🏜", "🌋", "⛰", "🏔", "🗻", "🏕", "⛺️", "🛖", "🏠", "🏡", "🏘", "🏚", "🏗", "🏭", "🏢", "🏬", "🏣", "🏤", "🏥", "🏦", "🏨", "🏪", "🏫", "🏩", "💒", "🏛", "⛪️", "🕌", "🕍", "🛕", "🕋", "⛩", "🛤", "🛣", "🗾", "🎑", "🏞", "🌅", "🌄", "🌠", "🎇", "🎆", "🌇", "🌆", "🏙", "🌃", "🌌", "🌉", "🌁", "🍏", "🍎", "🍐", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🫐", "🍈", "🍒", "🍑", "🥭", "🍍", "🥥", "🥝", "🍅", "🍆", "🥑", "🥦", "🫛", "🥬", "🥒", "🌶", "🫑", "🌽", "🥕", "🫒", "🧄", "🧅", "🫚", "🥔", "🫘", "🥐", "🥯", "🍞", "🥖", "🥨", "🧀", "🥚", "🍳", "🧈", "🥞", "🧇", "🥓", "🥩", "🍗", "🍖", "🦴", "🌭", "🍔", "🍟", "🍕", "🫓", "🥪", "🥙", "🧆", "🌮", "🌯", "🫔", "🥗", "🥘", "🫕", "🥫", "🍝", "🍜", "🍲", "🍛", "🍣", "🍱", "🥟", "🦪", "🍤", "🍙", "🍚", "🍘", "🍥", "🥠", "🥮", "🍢", "🍡", "🍨", "🍦", "🥧", "🧁", "🍰", "🎂", "🍮", "🍭", "🍬", "🍫", "🍿", "🍩", "🍪", "🌰", "🥜", "🍯", "🥛", "🍼", "🫖", "☕️", "🍵", "🧃", "🥤", "🧋", "🫙", "🍶", "🍺", "🍻", "🥂", "🍷", "🫗", "🥃", "🍸", "🍹", "🧉", "🍾", "🧊", "🥄", "🍴", "🍽", "🥣", "🥡", "🥢", "🧂", "⚽️", "🏀", "🏈", "⚾️", "🥎", "🎾", "🏐", "🏉", "🥏", "🎱", "🪀", "🏓", "🏸", "🏒", "🏑", "🥍", "🏏", "🪃", "🥅", "⛳️", "🪁", "🏹", "🎣", "🤿", "🥊", "🥋", "🎽", "🛹", "🛼", "🛷", "⛸", "🥌", "🎿", "🏆", "🥇", "🥈", "🥉", "🏅", "🎖", "🏵", "🎗", "🎫", "🎟", "🎪", "🤹", "🤹‍♂️", "🤹‍♀️", "🎭", "🩰", "🎨", "🎬", "🎤", "🎧", "🎼", "🎹", "🥁", "🪘", "🪇", "🎷", "🎺", "🪗", "🎸", "🪕", "🎻", "🎲", "♟", "🎯", "🎳", "🎮", "🎰", "🧩", "🪱", "🐛", "🦋", "🐌", "🐞", "🐜", "🪰", "🪲", "🪳", "🦟", "🦗", "🕷", "🕸", "🦂", "🐢", "🐍", "🦎", "🦖", "🦕", "🐙", "🦑", "🦐", "🦞", "🦀", "🪼", "🪸", "🐡", "🐠", "🐟", "🐬", "🐳", "🐋", "🦈", "🐅", "🐆", "🦓", "🫏", "🦍", "🦧", "🦣", "🐘", "🦛", "🦏", "🐪", "🐫", "🦒", "🦘", "🦬", "🐃", "🐂", "🐄", "🐎", "🐖", "🐏", "🐑", "🦙", "🐐", "🦌", "🫎", "🐕", "🐩", "🦮", "🐕‍🦺", "🐈", "🐈‍⬛", "🪽", "🪶", "🐓", "🦃", "🦤", "🦚", "🦜", "🦢", "🪿", "🦩", "🕊", "🐇", "🦝", "🦨", "🦡", "🦫", "🦦", "🦥", "🐁", "🐀", "🐿", "🦔", "🐾", "🐉", "🐲", "🌵", "🎄", "🌲", "🌳", "🌴", "🪹", "🪺", "🌱", "🌿", "☘️", "🍀", "🎍", "🪴", "🎋", "🍃", "🍂", "🍁", "🍄", "🐚", "🪨", "🌾", "💐", "🌷", "🪷", "🌹", "🥀", "🌺", "🌸", "🪻", "🌼", "🌻", "🌞", "🌝", "🌛", "🌜", "🌚", "🌕", "🌖", "🌗", "🌘", "🌑", "🌒", "🌓", "🌔", "🌙", "🌎", "🌍", "🌏", "🪐", "💫", "⭐️", "🌟", "✨", "⚡️", "☄️", "💥", "🔥", "🌪", "🌈", "☀️", "🌤", "⛅️", "🌥", "☁️", "🌦", "🌧", "⛈", "🌩", "🌨", "❄️", "☃️", "⛄️", "🌬", "💨", "💧", "💦", "🫧", "☔️", "☂️", "🌊"
            ],
            selectedBlock: 7,
            selectedBlock_item: -1,
            // selectedEmoji: ['👵🏻', '👋', '✌️', '👔', '👖', '🥿', '👠'],
            showEditPanelRec: {}, // 记录哪个人物展开了编辑面板
            showEditPanelRec_item: {}, // 记录哪个物品展开了编辑面板
            all_character_and_item: [
                {
                    characters: [],
                    items: [],
                }
            ],
            // characters: [
            //     // {
            //     //     // selectedBlock: 7,
            //     //     selectedEmoji: ['👩🏻‍🦳', '🫲🏻', '👗', '🫱🏻', '👖', '👠', '👠'], // 0: head, 1: left hand, 2: clothes, 3: right hand, 4: pants, 5: left foot, 6: right foot
            //     //     name: "grandma",
            //     // },
            //     // {
            //     //     // selectedBlock: 7,
            //     //     selectedEmoji: ['👵🏻', '👋', '👔', '✌️', '', '', ''],
            //     //     name: "grandpa",
            //     // },
            // ],
            // items: [
            //     // {
            //     //     selectedEmoji: '🏰',
            //     //     name: "castle",
            //     // },
            //     // {
            //     //     selectedEmoji: '🗝️',
            //     //     name: "key",
            //     // }
            // ],
            lastClicked: {}, // 选中的人物的id
            clickTimeout: null,
            isPlay: false, // 右侧原子操作面板是否展开的 flag
            // scenes: [], // 记录每一步动画后的信息
            all_scenes: [],
            userAnimationsCache: [], // 记录用户场景到场景的动画
            // animationList: [], // 记录最终播放的所有动画
            all_animationList: [
                []
            ], // 记录所有的动画
            showAnimationList: true, // 是否展示动画列表,
            currentFrameIndex: 0,
            // svo_list: [],
            all_svo_list: [
                []
            ],
            all_styles: [
                []
            ]
        };
    },
    mounted() {
        this.$bus.$on('initialize', (data) => {
            // data 是所有场景信息
            this.all_character_and_item = [];
            this.all_svo_list = [];
            this.all_animationList = [];
            this.all_scenes = [];
            this.all_styles = [];

            data.forEach((scene_info) => {
                let characters = [];
                let items = [];

                scene_info['character'].forEach((character) => {
                    characters.push({
                        selectedEmoji: ['👩🏻‍🦳', '🫲🏻', '👗', '🫱🏻', '👖', '👠', '👠'],
                        name: character, // character 本身就是name
                    });
                });

                scene_info['object'].forEach((item) => {
                    items.push({
                        selectedEmoji: '🍪',
                        name: item,
                    });
                });

                this.all_character_and_item.push({
                    characters: characters,
                    items: items,
                });

                this.all_svo_list.push([]);
                this.all_animationList.push([]);
                this.all_scenes.push([]);
                this.all_styles.push([]);

                this.currentFrameIndex = 0;
            });
            this.$nextTick(() => {
                this.animateShape();
            });
        });
        this.$bus.$on('switch_frame', (data) => {
            const scene_info = data[0]; // 一个场景的所有信息
            const scene_index = data[1]; // 当前场景的 index, 从 0 开始

            this.currentFrameIndex = scene_index;
            this.userAnimationsCache = [];

            console.log('收到 switch_frame', scene_info);

            this.all_character_and_item[this.currentFrameIndex]['characters'].forEach((_, index) => { // 初始化
                this.$set(this.showEditPanelRec, index, false);
            });

            this.all_character_and_item[this.currentFrameIndex]['items'].forEach((_, index) => { // 初始化
                this.$set(this.showEditPanelRec_item, index, false);
            });
            this.$nextTick(() => {
                this.animateShape();
            });
        });
        this.$bus.$on('select_design', (data) => {
            console.log('收到 select_design', data);
            const scene_info = data['scene']; // 一个场景的所有信息
            const svo_index = data['svo_index']; // 当前选中的 SVO 的 index
            const design_selection = data['design_selection']; // 当前选中的设计

            const action_type = design_selection.split(/_(.+)/)[0];
            const design_type = design_selection.split(/_(.+)/)[1];

            const svo = scene_info['svo'][svo_index];
            const characters = scene_info['character'];
            const items = scene_info['object'];

            const subject = svo['subject'];
            const verb = svo['verb'];
            const object = svo['object'];
            this.all_svo_list[this.currentFrameIndex].push(subject + ' ' + verb + ' ' + object);

            const character_index = characters.indexOf(subject);
            const characterId = "character-" + character_index; // character-0, character-1, ...

            const object_index = items.indexOf(object);
            const objectId = "item-" + object_index; // item-0, item-1, ...

            console.log("characterId: ", characterId);

            // atrans, expel, ingest, mental, move, propel, ptrans, speak
            if (action_type === "atrans") {
                if (design_type === 'all_path') {
                    const giverId = characterId;
                    const receiver = svo['receiver'];
                    const receiver_index = characters.indexOf(receiver);
                    const receiverId = "character-" + receiver_index; // character-0, character-1, ...
                    this.atrans(giverId, receiverId, objectId);
                }
            } else if (action_type === "expel") {
                if (design_type === 'all_appear-path') {
                    this.cry(characterId);
                }
            } else if (action_type === "ingest") {
                null;
            } else if (action_type === "mental") {
                if (design_type === "all_thought bubble") {
                    this.thought(characterId, objectId);
                }
            } else if (action_type === "move") {
                // feet_drub, feet_kick, feet_raise, feet_walk, hand_raise, hand_wave, head_nod, head_shake
                if (design_type === "feet_drub") {
                    null;
                } else if (design_type === "feet_kick") {
                    this.kickFoot(this.lastClicked); // 需要选中脚
                } else if (design_type === "feet_raise") {
                    null;
                } else if (design_type === "feet_walk") {
                    this.walk(characterId);
                } else if (design_type === "hand_raise") {
                    this.rotateHand(this.lastClicked); // 需要选中手
                } else if (design_type === "hand_wave") {
                    this.waveHand(this.lastClicked); // 需要选中手
                } else if (design_type === "head_nod") {
                    this.node_head(characterId);
                } else if (design_type === "head_shake") {
                    this.move_head(characterId);
                }
            } else if (action_type === "propel") {
                null;
            } else if (action_type === "ptrans") {
                if (design_type === "all_path") {
                    this.customizeMove(characterId);
                }
            } else if (action_type === "speak") {
                if (design_type === "all_dialogue box") {
                    console.log("all_dialogue box", characterId);
                    this.speak(characterId, object);
                }
            }

        });
    },
    methods: {
        removeEmoji(index) {
            this.$set(this.characters[index].selectedEmoji, this.selectedBlock, '');
        },
        removeEmoji_item(index) {
            // this.$set(this.items[index].selectedEmoji, '');
            this.items[index].selectedEmoji = '';
        },
        changeEditPanelRec(index) {
            this.$set(this.showEditPanelRec, index, !this.showEditPanelRec[index]);
            this.selectedBlock = 7;
        },
        changeEditPanelRec_Item(index) {
            this.$set(this.showEditPanelRec_item, index, !this.showEditPanelRec_item[index]);
            this.selectedBlock_item = -1;
        },
        clickBlock(index) {
            this.selectedBlock = index;
        },
        clickBlockItem() {
            this.selectedBlock_item = 1;
        },
        changeEmoji(index, characterIndex) {
            if (this.selectedBlock === -1) {
                return;
            }
            this.$set(this.all_character_and_item[this.currentFrameIndex]['characters'][characterIndex].selectedEmoji, this.selectedBlock, this.emojis[this.selectedBlock][index]);
        },
        changeEmoji_Item(emoji, index) {
            if (this.selectedBlock_item === -1) {
                return;
            }
            this.all_character_and_item[this.currentFrameIndex]['items'][index].selectedEmoji = emoji;
        },
        animateShape() {
            Draggable.create(['.character_in_story', '#emoji_1', '.item_in_story'], {
                bounds: document.getElementById("story_board"),
                inertia: true,
                zIndexBoost: false
            });
        },
        atrans(giverId, receiverId, itemId, resolve = null) { // transfer of abstract relationship 
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            // 获取 DOM 元素
            var giver = document.getElementById(giverId);
            var receiver = document.getElementById(receiverId);
            var item = document.getElementById(itemId);

            // 计算 giver 和 receiver 的位置
            var giverRect = giver.getBoundingClientRect();
            var receiverRect = receiver.getBoundingClientRect();

            // 计算 item 应该移动的距离
            var translateX = receiverRect.left - giverRect.left;
            var translateY = receiverRect.top - giverRect.top;

            // 使用 GSAP 创建动画
            // gsap.to(giver, { x: 100, duration: 1 });
            gsap.to(item, { x: "+=" + translateX, y: "+=" + translateY, duration: 1, onComplete: resolve });

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.atrans, args: [giverId, receiverId, itemId], name: "atrans" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        ptrans_appear(objectId, positionId) {
            // 获取 DOM 元素
            // var object = document.getElementById(objectId);
            // var position = document.getElementById(positionId);

            // 获取 DOM 元素
            var object = document.getElementById(objectId);
            var position = document.getElementById(positionId);

            // 计算 object 和 position 的位置
            var objectRect = object.getBoundingClientRect();
            var positionRect = position.getBoundingClientRect();

            // 计算 object 应该移动的距离
            var translateX = positionRect.left - objectRect.left;
            var translateY = positionRect.top - objectRect.top;

            var tl = gsap.timeline();

            tl.to(object, { autoAlpha: 0, repeat: 3, yoyo: true, duration: 0.3 });
            tl.set(object, { x: "+=" + translateX, y: "+=" + translateY, autoAlpha: 1, duration: 0.1 });
        },
        ptrans(objectId, positionId, resolve = null) { // transfer of physical location of object
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }
            // 获取 DOM 元素
            var object = document.getElementById(objectId);
            var position = document.getElementById(positionId);

            // 计算 object 和 position 的位置
            var objectRect = object.getBoundingClientRect();
            var positionRect = position.getBoundingClientRect();

            // 计算 object 应该移动的距离
            var translateX = positionRect.left - objectRect.left;
            var translateY = positionRect.top - objectRect.top;

            // 使用 GSAP 创建动画
            gsap.to(object, { x: "+=" + translateX, y: "+=" + translateY, duration: 1, onComplete: resolve });

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.ptrans, args: [objectId, positionId] });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        speak(characterId, text, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            let character = document.getElementById(characterId);
            // 创建对话框元素
            const speechBubble = document.createElement('p');
            speechBubble.classList.add('bubble', 'speech');
            speechBubble.textContent = text;
            // speechBubble.textContent = "Qui inventore asperiores ipsum asperiores. Ullam voluptas quia quia voluptatem accusantium iste corrupti. Voluptatum deserunt vitae iasperiores ipsum asperiores. Ullam voluptas quia quia voluptatem accusantium iste corrupti. Voluptatum deserunt vitae invnventore.";

            // 将对话框添加到角色元素
            character.appendChild(speechBubble);

            // 设置对话框的位置
            speechBubble.style.position = 'absolute';
            speechBubble.style.top = '-100px'; // 将top值调整为角色正上方的位置
            speechBubble.style.left = '60%';
            speechBubble.style.transform = 'translate(-10%, -100%)';

            setTimeout(() => {
                speechBubble.remove();
                resolve();
            }, 3000);

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.speak, args: [characterId, text], name: "speak" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        thought(characterId, text, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            let character = document.getElementById(characterId);
            // 创建对话框元素
            const speechBubble = document.createElement('p');
            speechBubble.classList.add('bubble', 'thought');
            speechBubble.textContent = text;
            // speechBubble.textContent = "Qui inventore asperiores ipsum asperiores. Ullam voluptas quia quia voluptatem accusantium iste corrupti. Voluptatum deserunt vitae iasperiores ipsum asperiores. Ullam voluptas quia quia voluptatem accusantium iste corrupti. Voluptatum deserunt vitae invnventore.";


            // 将对话框添加到角色元素
            character.appendChild(speechBubble);

            // 设置对话框的位置
            speechBubble.style.position = 'absolute';
            speechBubble.style.top = '-100px'; // 将top值调整为角色正上方的位置
            speechBubble.style.left = '60%';
            speechBubble.style.transform = 'translate(-5%, -100%)';

            setTimeout(() => {
                speechBubble.remove();
                resolve();
            }, 3000);

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.thought, args: [characterId, text], name: "thought" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        thought_2(characterId, text, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }


            let character = document.getElementById(characterId);
            // 创建对话框元素
            const speechBubble = document.createElement('div');
            speechBubble.classList.add('thought2');
            speechBubble.textContent = text;
            // speechBubble.textContent = "Qui inventore asperiores ipsum asperiores. Ullam voluptas quia quia voluptatem accusantium iste corrupti. Voluptatum deserunt vitae iasperiores ipsum asperiores. Ullam voluptas quia quia voluptatem accusantium iste corrupti. Voluptatum deserunt vitae invnventore.";


            // 将对话框添加到角色元素
            character.appendChild(speechBubble);

            // 设置对话框的位置
            speechBubble.style.position = 'absolute';
            speechBubble.style.top = '-60px'; // 将top值调整为角色正上方的位置
            speechBubble.style.left = '50%';
            speechBubble.style.transform = 'translate(-50%, -100%)';

            setTimeout(() => {
                speechBubble.remove();
                resolve();
            }, 3000);

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.thought_2, args: [characterId, text], name: "thought_2" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        scream(characterId, text, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            let character = document.getElementById(characterId);
            // 创建对话框元素
            const speechBubble = document.createElement('div');
            speechBubble.classList.add('electric');
            speechBubble.textContent = text;
            speechBubble.textContent = "Attack!";


            // 将对话框添加到角色元素
            character.appendChild(speechBubble);

            // 设置对话框的位置
            speechBubble.style.position = 'absolute';
            speechBubble.style.top = '-60px'; // 将top值调整为角色正上方的位置
            speechBubble.style.left = '50%';
            speechBubble.style.transform = 'translate(-100%, -100%)';

            setTimeout(() => {
                speechBubble.remove();
                resolve();
            }, 3000);

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.scream, args: [characterId, text], name: "scream" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        customizeMove(objectId) {  // ao_customized_move 右侧原子操作中的一个
            const vm = this;

            const object = document.getElementById(objectId);
            if (!object.classList.contains("character_in_story")) {
                return
            }
            var path = [];
            var svg; // SVG元素
            var polyline; // 折线元素

            var ghostElement;

            // const object = document.getElementById(objectId);
            const storyBoard = document.getElementById("story_board");

            var originalDraggable = Draggable.get(object); // 获取原有的Draggable实例
            if (originalDraggable) {
                originalDraggable.kill(); // 禁用原有的Draggable实例
            }

            Draggable.create(object, {
                type: "x,y",
                edgeResistance: 0.65,
                bounds: storyBoard,
                inertia: true,
                onPress: function () {
                    path = [];
                    // 创建SVG元素
                    svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
                    svg.style.position = "absolute";
                    svg.style.width = "100%";
                    svg.style.height = "100%";
                    storyBoard.appendChild(svg);
                    // 创建折线元素
                    polyline = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
                    polyline.setAttribute("stroke", "grey");
                    polyline.setAttribute("fill", "none");
                    polyline.setAttribute("stroke-width", "4");
                    polyline.setAttribute("stroke-dasharray", "5,5");
                    svg.appendChild(polyline);
                    // 创建一个幽灵元素
                    ghostElement = object.cloneNode(true);
                    ghostElement.id = "ghost";
                    ghostElement.style.opacity = 1;
                    ghostElement.style.pointerEvents = "none";
                    storyBoard.appendChild(ghostElement);
                    gsap.set(ghostElement, { x: this.x, y: this.y });
                    gsap.set(object, { opacity: 0.5 });
                },
                onDrag: function () {
                    path.push({ x: this.x, y: this.y });
                    // 更新折线路径
                    var points = path.map(point => `${point.x + object.offsetWidth / 2},${point.y + object.offsetHeight / 2}`).join(" ");
                    polyline.setAttribute("points", points);
                },
                onRelease: function () {
                    // 在释放元素时，移除SVG元素
                    svg.remove();

                    // 沿着轨迹运动
                    // var tl = gsap.timeline();
                    // tl.set(object, { opacity: 1 })
                    // tl.to(object, { x: path[0].x, y: path[0].y, duration: 0 });
                    // tl.to(object, {
                    //     motionPath: {
                    //         path: path,
                    //         curviness: 1.25,
                    //         // autoRotate: true
                    //     },
                    //     duration: 2
                    // });

                    vm.moveAlongPath(objectId, path);
                    ghostElement.remove();

                    if (originalDraggable) {
                        Draggable.create(object, originalDraggable.vars); // 恢复原有的Draggable实例
                    }

                }
            });
        },
        moveAlongPath(objectId, path, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            let object = document.getElementById(objectId);
            var tl = gsap.timeline();
            tl.set(object, { opacity: 1 })
            tl.to(object, { x: path[0].x, y: path[0].y, duration: 0 });
            tl.to(object, {
                motionPath: {
                    path: path,
                    curviness: 1.25,
                    // autoRotate: true
                },
                duration: 2
            });

            tl.eventCallback("onComplete", resolve);

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.moveAlongPath, args: [objectId, path], name: "move along path" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        propel_push(characterId, objectId) {
            // 角色的手部和物体同步运动，实现推的效果
            var object = document.getElementById(objectId);

            var right_hand = document.querySelector("#" + characterId + " .emoji_right_hand");
            var tl = gsap.timeline();
            tl.to([right_hand, object], { x: "+=100", duration: 1 });
            tl.to(right_hand, { x: "-=100", duration: 1 });
        },
        propel_pull(characterId, objectId, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }
            // 角色的手部和物体同步运动，实现拉的效果
            var object = document.getElementById(objectId);

            var right_hand = document.querySelector("#" + characterId + " .emoji_right_hand");
            var tl = gsap.timeline();
            tl.to([right_hand, object], { x: "-=100", duration: 1 });
            tl.to(right_hand, { x: "+=100", duration: 1 });


            tl.eventCallback("onComplete", resolve);

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.propel_pull, args: [characterId, objectId], name: "pull" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        propel_cast(characterId, objectId) {
            // 角色的手部和物体同步运动，实现投的效果
            var object = document.getElementById(objectId);

            var right_hand = document.querySelector("#" + characterId + " .emoji_right_hand");
            var tl = gsap.timeline();
            tl.to([right_hand, object], { y: "-=100", duration: 1 });
            tl.to(right_hand, { y: "+=100", duration: 1 });
        },
        move_head(objectId, range = 60, repeatTime = 4, duration = 0.4, resolve = null) { // 摇头
            let character = document.getElementById(objectId);
            let object = character.querySelector(".emoji_head");

            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            if (object === null) {
                console.log("object is null");
                resolve();
                return;
            }
            if (object.classList.contains("emoji_head") === false) {
                resolve();
                return;
            }
            gsap.fromTo(object, { rotateY: -range }, {
                rotateY: range, ease: "power1.inOut", repeat: repeatTime, yoyo: true, duration: duration, onComplete: function () {
                    gsap.to(object, { rotateY: 0, ease: "power1.inOut", duration: duration / 2, onComplete: resolve });
                }
            });

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.move_head, args: [objectId, range, repeatTime, duration], name: "shake head" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
            // resolve(); // 通知动画执行完毕
        },
        node_head(objectId, range = 60, repeatTime = 4, duration = 0.4, resolve = null) { // 点头
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            let character = document.getElementById(objectId);
            let object = character.querySelector(".emoji_head");
            if (object.classList.contains("emoji_head") === false) {
                resolve();
                return;
            }
            gsap.set(object, { transformOrigin: "50% 80%" });
            gsap.to(object, {
                rotateX: -range, ease: "power1.inOut", repeat: repeatTime, yoyo: true, duration: duration, onComplete: function () {
                    gsap.to(object, { rotateX: 0, ease: "power1.inOut", duration: duration, onComplete: resolve });
                }
            });

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.node_head, args: [objectId, range, repeatTime, duration], name: "nod head" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
            // resolve(); // 通知动画执行完毕
        },
        ingest(characterId, objectId, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            // 物体逐渐靠近角色，由大变小，最后消失
            var object = document.getElementById(objectId);
            var character = document.getElementById(characterId);

            var objectRect = object.getBoundingClientRect();
            var characterRect = character.getBoundingClientRect();

            // 计算 item 应该移动的距离
            var translateX = objectRect.left - characterRect.left - character.offsetWidth / 2;
            var translateY = objectRect.top - characterRect.top - character.offsetHeight / 2;

            // 使用 GSAP 创建动画
            gsap.to(object, {
                x: "-=" + translateX,
                y: "-=" + translateY,
                scale: 0,
                opacity: 0,
                duration: 1,
                onComplete: resolve,
            });

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.ingest, args: [characterId, objectId], name: "ingest" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        expel(characterId, objectId, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            // 物体逐渐远离角色，由消失变大
            var object = document.getElementById(objectId);
            // var character = document.getElementById(characterId);

            // var objectRect = object.getBoundingClientRect();
            // var characterRect = character.getBoundingClientRect();

            // 计算 item 应该移动的距离
            // var translateX = objectRect.left - characterRect.left;
            // var translateY = objectRect.top - characterRect.top;

            // 使用 GSAP 创建动画
            gsap.to(object, {
                x: "+=" + 100,
                y: "+=" + 100,
                scale: 1,
                opacity: 1,
                duration: 1,
                onComplete: resolve,
            });

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.expel, args: [characterId, objectId], name: "expel" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        ao_rotation(objectId) {
            let object = document.getElementById(objectId);
            if (!object.classList.contains("emoji_click")) {
                return
            }
            let originalDraggable = Draggable.get(object);
            if (originalDraggable) {
                originalDraggable.kill();
            }
            object.style.transformOrigin = '50% 50%';
            Draggable.create(object, {
                type: "rotation",
                edgeResistance: 1,
                inertia: true,
                onDrag: function () {
                    // console.log("dragging");
                },
                onDragEnd: function () {
                    // console.log("drag end");
                    if (originalDraggable) {
                        Draggable.create(object, originalDraggable.vars); // 恢复原有的Draggable实例
                    }
                }
            });
        },
        // ao_rotation() {
        //     window.addEventListener('click', this.rotateElement, { once: true });
        //     console.log(event);
        // },
        rotate_element(event) {
            console.log(event)
            event.stopPropagation();

            const element = event.target;
            gsap.to(element, { rotate: "+=" + 360, duration: 2 });
        },
        ao_scale(objectId) {
            let object = document.getElementById(objectId);

            let originalDraggable = Draggable.get(object);
            if (originalDraggable) {
                originalDraggable.kill();
            }
            let y;
            Draggable.create(object, {
                type: "top",
                edgeResistance: 0.65,
                onPress: function () {
                    y = object.offsetTop
                },
                onDrag: function () {
                    const scale = 1 + ((- this.y + y) / 50); // 调整此处的比例以控制缩放速度
                    gsap.set(object, { scale: scale, transformOrigin: "center center" });
                },
                onDragEnd: function () {
                    if (originalDraggable) {
                        Draggable.create(object, originalDraggable.vars); // 恢复原有的Draggable实例
                    }
                }
            });
        },
        ao_flip(objectId) {
            let object = document.getElementById(objectId);
            // const object = document.getElementById(objectId);
            gsap.to(object, { rotationY: "+=" + 180, duration: 2 });
        },
        ao_disappear(objectId) {
            const object = document.getElementById(objectId);
            gsap.set(object, { opacity: 0 });
        },
        ao_appear(objectId) {
            const object = document.getElementById(objectId);
            gsap.set(object, { opacity: 1 });
        },
        handle_emoji_click(event) {
            if (this.clickTimeout !== null) {
                clearTimeout(this.clickTimeout);
                this.clickTimeout = null;
                this.handleDoubleClick(event);
            } else {
                this.clickTimeout = setTimeout(() => {
                    this.clickTimeout = null;
                    this.handleSingleClick(event);
                }, 250); // 250毫秒内没有第二次点击则视为单击
            }
        },

        handleDoubleClick(event) { // 双击触发
            console.log("double click")
            if (event.target.classList.contains("emoji_click")) {
                // Add your logic here for when event.target belongs to class "emoji_click"
                this.lastClicked = event.target.id;
                console.log("this.lastClicked: ", this.lastClicked);
            }
        },
        handleSingleClick(event) { // 单击触发
            console.log("single click")
            if (event.target.classList.contains("item_in_story")) {
                // Add your logic here for when event.target belongs to class "emoji_click"
                this.lastClicked = event.target.id;
                console.log("this.lastClicked: ", this.lastClicked);
                return;
            }
            if (event.target.classList.contains("emoji_click")) {
                // Add your logic here for when event.target belongs to class "emoji_click"
                this.lastClicked = event.target.parentNode.id;
                console.log("this.lastClicked: ", this.lastClicked);
            }
        },
        footMove(objectId, step_frequency = 0.8) { // 添加人物运动时的脚步动画
            let object = document.getElementById(objectId);
            if (object.querySelector(".emoji_left_foot") === null) {
                return;
            }
            // 获取object 的子dom元素，并利用class筛选
            const left_foot = object.querySelector(".emoji_left_foot");
            const foot = object.querySelector(".emoji_right_foot");
            const footHeight = foot.getBoundingClientRect().height;
            const span = 0.3; // 步幅
            const height = 0.5; // 抬脚高度
            const frequency = step_frequency; // 步频


            // 创建一个无限循环的时间线
            var tl2 = gsap.timeline({ repeat: -1 });

            // 设置元素的初始位置为B点
            tl2.set(foot, { x: 2 * span * footHeight, y: 0 });

            // B -> C
            var path_bc = [
                { x: 2 * span * footHeight, y: 0 },
                { x: -2 * span * footHeight, y: 0 }
            ]
            tl2.to(foot, {
                duration: frequency,
                motionPath: {
                    path: path_bc,
                    curviness: 0
                    // autoRotate: true
                },
                ease: "power1.inOut"
            });

            // C -> D -> B
            var path_cdb = [
                { x: -2 * span * footHeight, y: 0 },
                { x: 0, y: -height * footHeight },
                { x: 2 * span * footHeight, y: 0 }
            ];
            tl2.to(foot, {
                duration: frequency,
                motionPath: {
                    path: path_cdb,
                    curviness: 1.25,
                    // autoRotate: true
                },
                ease: "power1.inOut"
            });

            // left foot
            tl2.set(left_foot, { x: -2 * span * footHeight, y: 0 }, 0);
            tl2.to(left_foot, {
                duration: frequency,
                motionPath: {
                    path: path_cdb,
                    curviness: 1.25,
                    // autoRotate: true
                },
                ease: "power1.inOut"
            }, 0);

            tl2.to(left_foot, {
                duration: frequency,
                motionPath: {
                    path: path_bc,
                    curviness: 0,
                    // autoRotate: true
                },
                ease: "power1.inOut"
            }, frequency);

            return [tl2, span, footHeight];
        },
        shake(objectId, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            let object = document.getElementById(objectId);
            if (object.classList.contains("character_in_story") === true || object.classList.contains("emoji_click") === true) {
                // const width = object.getBoundingClientRect().width;
                const span = 5
                gsap.fromTo(object, 0.01, { x: "-=" + span }, { x: "+=" + span, repeat: 40 });
                gsap.fromTo(object, 0.02, { y: "-=" + span }, { y: "+=" + span, repeat: 20, onComplete: resolve });
            } else {
                resolve();
                return;
            }

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.shake, args: [objectId], name: "shake body" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        rotateHand(objectId, repeatTime = 5, duration = 0.5, resolve = null) { // 以手为中心旋转
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            let object = document.getElementById(objectId);
            if (object.classList.contains("emoji_left_hand") === true || object.classList.contains("emoji_right_hand") === true) {
                gsap.set(object, { transformOrigin: "50% 70%" });
                gsap.fromTo(object, duration, { rotation: -45 }, { rotation: 45, repeat: repeatTime, yoyo: true, ease: "power1.inOut", onComplete: function () { gsap.set(object, { rotation: 0, onComplete: resolve }) } });
            } else {
                resolve();
                return;
            }

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.rotateHand, args: [objectId, repeatTime, duration], name: "rotate hand" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        waveHand(objectId, repeatTime = 5, duration = 0.5, resolve = null) { // 以肘为中心旋转
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            let object = document.getElementById(objectId);
            if (object.classList.contains("emoji_left_hand") === true || object.classList.contains("emoji_right_hand") === true) {
                gsap.set(object, { transformOrigin: "50% 200%" });
                gsap.fromTo(object, duration, { rotation: -30 }, { rotation: 30, repeat: repeatTime, yoyo: true, ease: "power1.inOut", onComplete: function () { gsap.set(object, { rotation: 0, onComplete: resolve }) } });
            } else {
                resolve();
                return;
            }

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.waveHand, args: [objectId, repeatTime, duration], name: "wave hand" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        kickFoot(objectId, duration = 0.3, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            let object = document.getElementById(objectId);
            if (object.classList.contains("emoji_left_foot") === true || object.classList.contains("emoji_right_foot") === true) {
                gsap.set(object, { transformOrigin: "50% -200%" });
                gsap.to(object, duration, { rotation: -30, ease: "power1.inOut", yoyo: true, repeat: 1, onComplete: resolve });
            } else {
                console.log("object is not foot");
                resolve();
                return;
            }

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.kickFoot, args: [objectId, duration], name: "kick foot" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        jump(objectId, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            let object = document.getElementById(objectId);
            if (object.classList.contains("character_in_story") === true) {
                var tl = gsap.timeline();
                tl.set(object, { transformOrigin: "50% 100%" });
                tl.to(object, { scaleY: 0.9, duration: 0.5, ease: "power1.out" });
                tl.to(object, { scaleY: 1, y: "-=100", duration: 0.5, ease: "power1.out" });
                tl.to(object, { scaleY: 1, y: "+=100", duration: 0.5, ease: "power1.in" });
                tl.eventCallback("onComplete", resolve);
            } else {
                resolve();
                return;
            }

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.jump, args: [objectId], name: "jump" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        // walk(object, distance = 100, duration = 3, step_frequency = 1) {
        //     if (object.classList.contains("character_in_story") === true) {
        //         var foot_tl = this.footMove(object, step_frequency);
        //         var tl = gsap.timeline();
        //         tl.to(object, { x: "+=" + distance, duration: duration * 2 * step_frequency, ease: "power1.inOut", onComplete: function () { foot_tl.kill(); } });
        //     }
        // },
        walk(objectId, distance = 800, speed = 200, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            let object = document.getElementById(objectId);
            const k = 3; // 步频 必须是整数
            const step_frequency = distance / (speed * 2 * k);
            const duration = 2 * k * step_frequency;

            console.log("step_frequency: ", step_frequency);
            if (object === null) {
                console.log("object is null");
                resolve();
                return;
            }

            if (object.classList.contains("character_in_story") === true) {
                var [foot_tl, span, footHeight] = this.footMove(objectId, step_frequency);
                var tl = gsap.timeline();

                tl.to(object, {
                    x: "+=" + distance, duration: duration, ease: "power1.inOut", onComplete: function () {
                        foot_tl.kill();
                        gsap.to(object.querySelector(".emoji_right_foot"), { x: "-=" + 2 * span * footHeight, y: 0, duration: step_frequency / 2, ease: "power1.inOut" });
                        gsap.to(object.querySelector(".emoji_left_foot"), { x: "+=" + 2 * span * footHeight, y: 0, duration: step_frequency / 2, ease: "power1.inOut" });
                        resolve();
                    }
                });
            } else {
                resolve();
                return;
            }

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.walk, args: [objectId, distance, speed], name: "walk" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        cry(objectId, resolve = null) {
            const defaultResolve = () => { };
            if (resolve === null) {
                resolve = defaultResolve;
            }

            let object = document.getElementById(objectId);
            if (object.classList.contains("character_in_story") !== true) {
                resolve();
                return;
            }

            const head = object.querySelector(".emoji_head");

            // 创建两个新的 span 元素
            let span1 = document.createElement('div'); // 左眼
            let span2 = document.createElement('div'); // 右眼

            // 设置 span 元素的文本内容和样式
            span1.textContent = "💧";
            span1.style.position = "absolute";
            span2.textContent = "💧";
            span2.style.position = "absolute";

            // 设置span的水平定位中心
            span1.style.transform = "translate(-50%, 0%)";
            span2.style.transform = "translate(-50%, 0%)";

            // 将新的 span 元素添加为 object 的子元素
            object.appendChild(span1);
            object.appendChild(span2);

            let headRect = head.getBoundingClientRect();
            let headWidth = headRect.width;
            let headHeight = headRect.height;
            console.log("head.offsetLeft", head.offsetLeft);
            let span1_left = head.offsetLeft - headWidth * .21 + 'px';
            let span1_top = head.offsetTop + headHeight * .25 + 'px';
            let span2_left = head.offsetLeft + headWidth * .21 + 'px';
            let span2_top = head.offsetTop + headHeight * .25 + 'px';

            // 创建一个动画，使泪水向下移动
            gsap.fromTo(span1, { x: span1_left, y: span1_top }, {
                y: "+=" + headHeight * .7, opacity: 0, duration: 2, ease: "power1.in", repeat: 3, onComplete: function () {
                    span1.remove();
                    span2.remove();
                    resolve();
                }
            });
            gsap.fromTo(span2, { x: span2_left, y: span2_top }, { y: "+=" + headHeight * .7, opacity: 0, duration: 1, ease: "power1.in", repeat: 2 });

            if (resolve === defaultResolve) {
                this.userAnimationsCache.push({ func: this.cry, args: [objectId], name: "cry" });
                console.log("this.userAnimationsCache: ", this.userAnimationsCache);
            }
        },
        async runAnimations(animationList = []) { // 连续运行动画
            // animationList = [
            //     { func: this.walk, args: [document.getElementById("character-0"), 800, 200] },
            //     { func: this.jump, args: [document.getElementById("character-0")] }
            // ];

            // animationList = [
            //     [{ func: this.walk, args: ["character-0", 800, 200] },
            //     { func: this.jump, args: ["character-0"] }],
            //     [{ func: this.walk, args: ["character-0", 800, 200] },
            //     { func: this.jump, args: ["character-1"] }]
            // ];

            // animationList = [
            //     [{ func: this.walk, args: [document.getElementById("character-0"), 800, 200] }],
            //     [{ func: this.jump, args: [document.getElementById("character-0")] }]
            // ];

            // for (let i = 0; i < animationList.length; i++) {
            //     const animation = animationList[i];
            //     await new Promise((resolve) => {
            //         console.log("animation: ", animation.func, animation.args)
            //         animation.func(...animation.args, resolve);
            //     });
            // }
            this.loadScene(0); // 恢复到初始场景从头开始运行动画

            animationList = this.all_animationList[this.currentFrameIndex];

            for (let i = 0; i < animationList.length; i++) {
                const animation_small_list = animationList[i];
                await Promise.all(animation_small_list.map(animation => new Promise((resolve) => {
                    animation.func(...animation.args, resolve);
                })));
            }

            console.log('动画结束')

            // 在 JavaScript 中，异步（Asynchronous）和同步（Synchronous）是两种基本的执行模式。
            // **同步（Synchronous）**：在同步编程中，代码按照它在程序中出现的顺序执行。每个操作必须在下一个操作开始之前完成。如果一个操作需要花费很长时间（例如，读取大文件或从网络获取数据），那么程序将停止并等待该操作完成。
            // **异步（Asynchronous）**：在异步编程中，操作可以在后台运行，程序不需要等待它完成就可以继续执行其他操作。当异步操作完成时，程序将被通知并可以访问结果（例如，数据读取完毕或网络请求的响应已经到达）。
            // 在你的代码中，你使用了 `Promise` 和 `async/await` 来处理异步操作。`Promise` 是 JavaScript 中用于处理异步操作的一种对象。一个 `Promise` 代表一个尚未完成但预期在未来完成的操作。
            // `async/await` 是一种基于 `Promise` 的语法，用于编写看起来像同步代码的异步代码。`async` 关键字用于声明一个函数是异步的，而 `await` 关键字用于等待一个 `Promise` 完成。
            // 在你的代码中，你使用了 `Promise.all` 方法来等待一组 `Promise` 完成。`Promise.all` 接受一个 `Promise` 数组，并返回一个新的 `Promise`，这个新的 `Promise` 在所有输入的 `Promise` 都完成时解析。
            // 你的代码中的 `for` 循环中的每次迭代都会等待一组动画完成。这是通过创建一个 `Promise` 数组（每个动画一个 `Promise`），然后使用 `Promise.all` 等待所有这些 `Promise` 完成来实现的。`await` 关键字用于等待 `Promise.all` 返回的 `Promise` 完成，这意味着它会等待所有动画完成。然后，`for` 循环进入下一次迭代，开始下一组动画。
            // 这种方式允许你按顺序执行一组动画，每组动画中的所有动画可以同时开始，但下一组动画必须等待当前组动画全部完成才能开始。
        },
        // saveScene() {
        //     // 保存场景
        //     const clonedStoryBoard = document.getElementById("story_board").cloneNode(true);
        //     this.all_scenes[this.currentFrameIndex].push(clonedStoryBoard);
        //     this.userAnimationsCache = []; // 每次记录都要清空用户的动画缓存
        //     console.log("saveScene(): this.all_scenes: ", this.all_scenes);
        //     console.log("saveScene(): this.userAnimationsCache: ", this.userAnimationsCache);

        // },
        // loadScene(index = 0) {
        //     // 加载场景
        //     const clonedStoryBoard = this.all_scenes[this.currentFrameIndex][index].cloneNode(true);
        //     const storyBoard = document.getElementById("story_board");
        //     storyBoard.replaceWith(clonedStoryBoard);

        //     // 重新绑定事件
        //     this.animateShape();
        //     // 遍历 storyBoard子元素，并根据class筛选
        //     const items = clonedStoryBoard.querySelectorAll(".item_in_story");
        //     items.forEach(item => {
        //         item.addEventListener('click', event => this.handle_emoji_click(event));
        //     });

        //     const characters = clonedStoryBoard.querySelectorAll(".character_in_story");
        //     characters.forEach(character => {
        //         console.log(character);
        //         character.addEventListener('click', event => this.handle_emoji_click(event));
        //     });
        // },
        saveScene() {
            // 遍历story board中的子元素，push 样式 {id: style} 到 this.all_styles[currentFrameIndex]
            const story_board = document.getElementById("story_board");
            const items = story_board.querySelectorAll(".item_in_story");
            const characters = story_board.querySelectorAll(".character_in_story");

            let tmp = {}

            items.forEach(item => {
                // this.all_styles[this.currentFrameIndex][item.id] = item.style.cssText;
                let style = window.getComputedStyle(item);
                let styleObject = {};
                for (let property of style) {
                    styleObject[property] = style.getPropertyValue(property);
                }
                tmp[item.id] = styleObject;
            });

            characters.forEach(character => {
                // this.all_styles[this.currentFrameIndex][character.id] = character.style.cssText;
                let style = window.getComputedStyle(character);
                let styleObject = {};
                for (let property of style) {
                    styleObject[property] = style.getPropertyValue(property);
                }
                tmp[character.id] = styleObject;
            });

            this.all_styles[this.currentFrameIndex].push(tmp);

            console.log("saveScene(): this.all_styles: ", this.all_styles);
        },
        loadScene(index = 0) {
            // 加载场景
            // 从 this.all_styles[currentFrameIndex][index] 中恢复样式
            const styles = this.all_styles[this.currentFrameIndex][index];
            for (const [key, value] of Object.entries(styles)) {
                console.log(key, value);
                const element = document.getElementById(key);
                for (const [property, propertyValue] of Object.entries(value)) {
                    element.style[property] = propertyValue;
                }
            }

        },
        clearUserAnimationsCache() {
            this.userAnimationsCache = []; // 清空这一步的用户动画
            if (this.all_scenes[this.currentFrameIndex].length > 0) {
                this.loadScene(this.all_scenes[this.currentFrameIndex].length - 1); // 恢复到最后一个场景
            }
            console.log("this.userAnimationsCache: ", this.userAnimationsCache);
        },
        // async confirmUserAnimations() { // 确认这一步的用户动画: 1. 恢复到最后一个场景，预览用户动画，存储新场景 2. 存储用户动画到 this.animations 
        //     if (this.scenes === 0) { return; }
        //     if (this.userAnimationsCache.length === 0) { return; }

        //     // 我要将 userAnimationsCache 做为整体添加到 animationList 中
        //     // let tmp = this.animationList;
        //     // tmp.push(this.userAnimationsCache);
        //     this.animationList.push(this.userAnimationsCache);
        //     // this.animationList = tmp;
        //     // this.$set(this.animationList, this.animationList.length, this.userAnimationsCache);
        //     console.log("this.animationList: ", this.animationList);


        //     this.$nextTick()
        //         .then(() => {
        //             // 在这里，视图已经更新
        //             console.log('View updated');
        //         });

        //     this.loadScene(this.scenes.length - 1); // 恢复到最后一个场景

        //     console.log("this.userAnimationsCache: ", this.userAnimationsCache)
        //     // 预览用户动画
        //     for (const animation of this.userAnimationsCache) {
        //         await new Promise((resolve) => {
        //             console.log("animation: ", animation.func, animation.args)
        //             animation.func(...animation.args, resolve);
        //         });
        //     }

        //     // 存储新场景
        //     this.saveScene();
        //     this.userAnimationsCache = []; // 清空这一步的用户动画

        //     console.log("this.scenes: ", this.scenes);
        //     console.log("confirmed user animations");
        // },
        confirmUserAnimations() { // 确认这一步的用户动画: 1. 恢复到最后一个场景，预览用户动画，存储新场景 2. 存储用户动画到 this.animations 
            if (this.all_styles[this.currentFrameIndex].length === 0) { 
                console.log("this.all_styles[this.currentFrameIndex].length === 0");
                return; }
            if (this.userAnimationsCache.length === 0) { 
                console.log("this.userAnimationsCache.length === 0");
                return; 
            }

            // 我要将 userAnimationsCache 做为整体添加到 animationList 中
            // let tmp = this.animationList;
            // tmp.push(this.userAnimationsCache);
            this.all_animationList[this.currentFrameIndex].push(this.userAnimationsCache);
            // this.animationList = tmp;
            // this.$set(this.animationList, this.animationList.length, this.userAnimationsCache);
            console.log("this.all_animationList: ", this.all_animationList);


            // this.$nextTick()
            //     .then(() => {
            //         // 在这里，视图已经更新
            //         console.log('View updated');
            //     });

            // this.loadScene(this.scenes.length - 1); // 恢复到最后一个场景

            // console.log("this.userAnimationsCache: ", this.userAnimationsCache)
            // // 预览用户动画
            // for (const animation of this.userAnimationsCache) {
            //     await new Promise((resolve) => {
            //         console.log("animation: ", animation.func, animation.args)
            //         animation.func(...animation.args, resolve);
            //     });
            // }

            // 存储新场景
            this.saveScene();
            this.userAnimationsCache = []; // 清空这一步的用户动画

            console.log("this.all_scenes: ", this.all_scenes);
            console.log("confirmed user animations");
        }
    }
}
</script>

<style>
.emoji {
    width: 100px;
    height: 100px;
    position: absolute;
}

#design_board_character {
    width: 1800px;
    height: 200px;
    /* flex-shrink: 0; */
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    overflow-y: hidden;
}

#design_board_items {
    width: 1600px;
    height: 200px;
    /* flex-shrink: 0; */
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    overflow-y: hidden;
}

#story_board {
    border-radius: 20px;
    border: 2px solid #B2AAD1;
    width: 1600px;
    height: 900px;
    /* flex-shrink: 0; */
}

#control {
    border-radius: 20px;
    width: 100px;
    height: 900px;
    background-color: #AF99C7;
}

.boarder_style {
    border-radius: 20px;
    border: 2px solid #B2AAD1;
}

.control_button.test {
    width: 80px;
    height: 20px;
}

.control_button {
    width: 80px;
    height: 80px;
    margin: 10px;
}

.preview_block {
    width: 300px;
    height: 200px;
    flex-shrink: 0;
}

.emoji_head {
    width: 40px;
    height: 40px;
    font-size: 40px;
    position: absolute;
    top: 20px;
    left: 150px;

    transform: translate(-50%, -50%);

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */

}

.emoji_clothes {
    width: 40px;
    height: 40px;
    font-size: 40px;
    position: absolute;
    top: 60px;
    left: 150px;
    transform: translate(-50%, -50%);

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.emoji_left_hand {
    width: 25px;
    height: 25px;
    font-size: 25px;
    position: absolute;
    top: 60px;
    left: 115px;
    transform: translate(-50%, -50%);

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.emoji_right_hand {
    width: 25px;
    height: 25px;
    font-size: 25px;
    position: absolute;
    top: 60px;
    left: 185px;
    transform: translate(-50%, -50%);

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.emoji_pants {
    width: 40px;
    height: 40px;
    font-size: 40px;
    position: absolute;
    top: 100px;
    left: 150px;
    transform: translate(-50%, -50%);

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.emoji_left_foot {
    width: 25px;
    height: 25px;
    font-size: 25px;
    position: absolute;
    top: 135px;
    left: 140px;
    transform: translate(-50%, -50%);

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.emoji_right_foot {
    width: 25px;
    height: 25px;
    font-size: 25px;
    position: absolute;
    top: 135px;
    left: 165px;
    transform: translate(-50%, -50%);

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.emoji_head_no_legs {
    width: 64px;
    height: 64px;
    font-size: 64px;
    position: absolute;
    top: 40px;
    left: 150px;
    transform: translate(-50%, -50%);

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.emoji_clothes_no_legs {
    width: 76px;
    height: 76px;
    font-size: 76px;
    position: absolute;
    top: 110px;
    left: 150px;
    transform: translate(-50%, -50%);

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */

}

.emoji_left_hand_no_legs {
    width: 36px;
    height: 36px;
    font-size: 36px;
    position: absolute;
    top: 110px;
    left: 85px;
    transform: translate(-50%, -50%);

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.emoji_right_hand_no_legs {
    width: 36px;
    height: 36px;
    font-size: 36px;
    position: absolute;
    top: 110px;
    left: 205px;
    transform: translate(-50%, -50%);


    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}




.emoji_item {
    width: 100px;
    height: 100px;
    font-size: 100px;
    transform: translate(-50%, -50%);
    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.preview_name {
    color: #FFF;
    text-align: center;
    font-family: Montserrat;
    font-size: 40px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;

    text-transform: capitalize;

    width: 200px;
    height: 50px;

    display: flex;
    justify-content: center;
    align-items: center;
}

.edit_panel {
    width: 1600px;
    height: 900px;
    border-radius: 40px;
    border: 6px solid #7566A9;
    background-color: #FCF6F4;
    z-index: 999;
    box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.3);
}

.edit_panel_title {
    width: 1520px;
    height: 100px;

    color: #FFFCF9;
    font-family: Montserrat;
    font-size: 64px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;

    background-color: #7566A9;
    border-radius: 30px 30px 0px 0px;
    padding: 0px 40px;

    display: flex;
    align-items: center;
}

.edit_panel_name {
    color: #FFFCF9;
    font-family: Montserrat;
    font-size: 64px;
    font-style: italic;
    font-weight: 500;
    line-height: normal;

    text-transform: capitalize;
}

.small_block_small {
    width: 100px;
    height: 100px;
    font-size: 100px;

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.small_block_medium {
    width: 160px;
    height: 160px;
    font-size: 160px;

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.small_block_large {
    width: 200px;
    height: 200px;
    font-size: 200px;

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.small_block_XLarge {
    width: 240px;
    height: 240px;
    font-size: 240px;

    display: flex;
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
}

.small_block {
    border-radius: 16px;
    border: 2px dashed #7566A9;

}

.small_block_selected {
    border-radius: 16px;
    border: 4px solid #7566A9;
}

.small_block_occupied {
    border: none
}

.title_inventory {
    color: #7566A9;
    font-family: Montserrat;
    font-size: 84px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
}

.emoji_list {
    width: 800px;
    height: 400px;
    border-radius: 40px;
    border: 4px solid #7566A9;
    padding: 10px;
    overflow: auto;
}

.emoji_in_list {
    width: 80px;
    height: 80px;
    font-size: 80px;
    display: inline-block;
    cursor: pointer;
    margin: 0px 10px
}

.edit_panel_bt_container {
    width: 200px;
    height: 100px;
    display: flex;
    background-color: #FCF6F4;
    border-radius: 0px 0px 40px 0px;
}

.edit_panel_button {
    width: 80px;
    height: 80px;
    margin: 10px 10px;
}

.character_in_story {
    width: 300px;
    height: 200px;
    border: 2px solid #7566A9;
}


p.bubble {
    position: relative;
    width: 300px;
    text-align: center;
    line-height: 1.4em;
    margin: 40px auto;
    background-color: #fff;
    border: 8px solid #333;
    border-radius: 30px;
    font-family: sans-serif;
    padding: 20px;
    font-size: large;
}

p.thought {
    width: 300px;
    border-radius: 200px;
    padding: 30px;
}

p.bubble:before,
p.bubble:after {
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
}

p.speech:before {
    left: 30px;
    bottom: -50px;
    border: 25px solid;
    border-color: #333 transparent transparent #333;
}

p.speech:after {
    left: 38px;
    bottom: -30px;
    border: 15px solid;
    border-color: #fff transparent transparent #fff;
}

p.thought:before,
p.thought:after {
    left: 10px;
    bottom: -30px;
    width: 40px;
    height: 40px;
    background-color: #fff;
    border: 8px solid #333;
    -webkit-border-radius: 28px;
    -moz-border-radius: 28px;
    border-radius: 28px;
}

p.thought:after {
    width: 20px;
    height: 20px;
    left: 5px;
    bottom: -40px;
    -webkit-border-radius: 18px;
    -moz-border-radius: 18px;
    border-radius: 18px;
}

.thought2 {
    display: flex;
    background-color: #B2AAD1;
    padding: 20px;
    border-radius: 30px;

    width: 300px;
    min-height: 40px;
    margin: 20px;
    position: relative;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.thought2:before,
.thought2:after {
    content: "";
    background-color: #B2AAD1;
    border-radius: 50%;
    display: block;
    position: absolute;
    z-index: -1;
}

.thought2:before {
    width: 44px;
    height: 44px;
    top: -12px;
    left: 28px;
    box-shadow: -50px 30px 0 -12px #B2AAD1;
}

.thought2:after {
    bottom: -10px;
    right: 26px;
    width: 30px;
    height: 30px;
    box-shadow: 40px -34px 0 0 #B2AAD1,
        -28px -6px 0 -2px #B2AAD1,
        -24px 17px 0 -6px #B2AAD1,
        -5px 25px 0 -10px #B2AAD1;

}

div.electric {
    background: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/4273/electric.svg);
    width: 400px;
    font-size: 2.4vw;
    font-style: italic;
    padding: 4% 6% 4% 4%;
}

div.electric span {
    display: block;
    font-size: 3vw;
    font-weight: bold;
}

.color_block {
    border-radius: 0px 0px 20px 20px;
    background-color: #7566A9;
    width: 300px;
    height: 50px;
}

.animation_list {
    width: 600px;
    height: 900px;
    flex-shrink: 0;

    border-radius: 20px;
    border: 2px solid #B2AAD1;
    background: #FFFCF9;
}

.animation_list_title {
    border-radius: 20px 20px 0px 0px;
    background: #7566A9;
    color: #FFF;
    text-align: center;
    font-family: Montserrat;
    font-size: 38px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
}

.animation_title {
    width: 496px;
    height: 96px;
    flex-shrink: 0;

    background-color: #FFFCF9;
    border: solid 2px #B2AAD1;
    border-radius: 10px;

    color: var(--color-black, #000);
    text-align: center;
    font-family: Montserrat;
    font-size: 32px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;

    display: flex;
    justify-content: center;
    align-items: center;
}

.animation_title_index {
    width: 100px;
    height: 100px;

    color: #FFF;
    text-align: center;
    font-family: Montserrat;
    font-size: 48px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;

    display: flex;
    justify-content: center;
    align-items: center;
}

.animation_subaction {
    width: 596px;
    height: 46px;
    flex-shrink: 0;

    background-color: #FFFCF9;
    border: solid 2px #B2AAD1;
    border-radius: 10px;

    color: var(--color-black, #000);
    text-align: center;
    font-family: Montserrat;
    font-size: 32px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    text-transform: capitalize;

    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
