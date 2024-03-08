<template>
  <div class="mainPage">
    <div class="userSelect">
      用户选择：<a-select
        style="width: 120px"
        default-value="coin"
        :options="user_list"
        @change="userSelectChange"
      >
      </a-select>
    </div>
    <div class="userContent">
      <a-card
        v-if="update"
        :loading="card_loadind"
        id="contentCard"
        title="Card title"
        :tab-list="tabList"
        :active-tab-key="now_tab"
        @tabChange="(key) => onTabChange(key)"
      >
        <template #customRender="item">
          <span>
            <HomeOutlined v-if="item.type == 'home'" />
            <LineChartOutlined v-else-if="item.type == 'line-chart'" />
            <SettingOutlined v-else-if="item.type == 'setting'" />
            {{ item.name }}
          </span>
        </template>
        <template #extra>
          <a href="#">返回coin的垃圾桶</a>
        </template>
        <router-view />
      </a-card>
    </div>
  </div>
</template>
<script>
import { getUserList } from "../../api/requests";
import {
  HomeOutlined,
  LineChartOutlined,
  SettingOutlined,
} from "@ant-design/icons-vue";
export default {
  inject: ["initEvery"],
  components: {
    HomeOutlined,
    LineChartOutlined,
    SettingOutlined,
  },
  data() {
    return {
      card_loadind: false,
      update: true,
      tabList: [
        {
          key: "0",
          name: "每日打卡",
          slots: { tab: "customRender" },
          type: "home",
          path_name: "Everyday",
        },
        {
          key: "1",
          name: "数据统计",
          slots: { tab: "customRender" },
          type: "line-chart",
          path_name: "DataStatistics",
        },
        {
          key: "2",
          name: "个人设置",
          slots: { tab: "customRender" },
          type: "setting",
          path_name: "Setting",
        },
      ],
      now_tab: "0",
      user_list: [],
    };
  },
  methods: {
    reload() {
      // 移除组件
      this.update = false;
      // 在组件移除后，重新渲染组件
      // this.$nextTick可实现在DOM 状态更新后，执行传入的方法。
      this.$nextTick(() => {
        this.update = true;
      });
    },
    onTabChange(key) {
      this.now_tab = key;
      this.$router.push({ name: this.tabList[parseInt(key)].path_name });
    },
    afterGetUserList(res) {
      this.user_list = res.data.user_name;
    },
    userSelectChange(value) {
      // TODO:
      //在切换用户的时候 要刷新其他组件的内容
      this.$store.state.now_user = value;
      this.reload();
    },
    initPage() {
      // this.$store.state.now_user='coin';
    },
  },
  created() {
    getUserList().then(this.afterGetUserList);
  },
  mounted() {
    this.initPage();
  },
  computed: {
    now_user() {
      return this.$store.state.now_user;
    },
  },
};
</script>
<style lang="scss">
.mainPage {
  padding: 2% 5%;
  // text-align: center;
}
.userContent {
  padding: 2% 5%;
  #contentCard {
    width: 100%;
    min-height: 800px;
  }
}
</style>