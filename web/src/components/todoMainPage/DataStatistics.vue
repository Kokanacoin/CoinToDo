<template>
  <div>
    <div class="calendar">
      <a-calendar
        v-model:value="data_value"
        @panelChange="calendarChange(data_value)"
      >
        <template #dateCellRender="{ current: data_value }">
          <div v-for="item in showStatisticData(data_value)" :key="item.key">
            <a-popover>
              <template #content>
                <div class="tooltips">
                  <ul class="events">
                    <li v-for="each in item.tooltips" :key="each.task">
                      <a-badge :status="each.state" :text="each.task" />
                    </li>
                  </ul>
                </div>
              </template>

              <a-progress
                class="progress"
                stroke-linecap="square"
                :percent="item.persent"
                type="dashboard"
                :width="80"
                :format="() => item.text"
                :stroke-color="{
                  '0%': '#108ee9',
                  '100%': '#87d068',
                }"
              />
            </a-popover>
          </div>
        </template>

        <!-- <template #monthCellRender="{ current: value }">
      <div v-if="getMonthData(value)" class="notes-month">
        <section>{{ getMonthData(value) }}</section>
        <span>Backlog number</span>
      </div>
    </template> -->
      </a-calendar>
    </div>
  </div>
</template>
<script>
import { getStatisticData } from "../../api/requests";
export default {
  data() {
    return {
      data_value: null,
      sta_data: {},
    };
  },
  methods: {
    initStatistics() {
      console.log("initStatistics");
    },
    calendarChange(render) {
      this.sta_data = {};
      getStatisticData({
        date: render.format("YYYY-MM-DD"),
        now_user: this.$store.state.now_user,
      }).then(this.afterCalendarChange);
    },
    afterCalendarChange(res) {
      this.sta_data = res.data;
    },

    showStatisticData(value) {
        console.log("date_" + value.month() + "_" + value.date());
      return this.sta_data["date_" + value.month() + "_" + value.date()] || [];
    },
  },
  created() {
    this.initStatistics();
  },
  mounted() {
    let now = new Date();
    let date_n = `${now.getFullYear()}-${now.getMonth() + 1}-${now.getDate()}`;
    getStatisticData({
      date: date_n,
      now_user: this.$store.state.now_user,
    }).then(this.afterCalendarChange);
  },
};
</script>
<style lang="scss" scoped>
.calendar {
  .progress {
    margin-left: 25%;
  }
}

.tooltips {
  .events {
    list-style: none;
    margin: 0;
    padding: 0;
  }
}
</style>