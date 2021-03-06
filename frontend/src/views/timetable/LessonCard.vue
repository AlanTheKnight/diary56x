<template>
  <div class="card mb-3 card-body" v-if="day.lessons.length != 0">
    <div class="card-title text-center">
      <div v-if="isToday">
        <h4>Расписание на сегодня</h4>
      </div>
      <div v-else-if="isTomorrow">
        <h4>Расписание на завтра</h4>
      </div>
      <div v-else>
        <h4>{{ getDayName(day.weekday) }}</h4>
      </div>
    </div>
    <div v-for="(lesson, index) in timetable" :key="lesson.id">
      <div class="row mt-1">
        <div class="col-2 text-center">
          <div v-if="lesson.subject.icon" class="subject-icon-wrapper">
            <img class="subject-icon" :src="lesson.subject.icon" alt="" />
          </div>
        </div>
        <div class="col" style="position: relative">
          <div style="position: absolute; top: 0; right: 1rem; text-align: end">
            <div>#{{ lesson.n }}</div>
            <div>
              {{ renderTime(lesson.start) }} - {{ renderTime(lesson.end) }}
            </div>
          </div>
          <div class="subject-name">
            <b>{{ lesson.subject.name }}</b>
          </div>
          <div v-if="lesson.classrooms instanceof Array">
            <table
              class="table table-sm mb-0 mt-1 classrooms-table"
              style="width: fit-content"
              v-if="lesson.classrooms.length !== 0"
            >
              <tbody>
                <tr v-for="classroom in lesson.classrooms">
                  <template v-if="classroom.includes('-')">
                    <td>{{ classroom.split("-").map((l) => l.trim())[0] }}</td>
                    <td>{{ classroom.split("-").map((l) => l.trim())[1] }}</td>
                  </template>
                  <td v-else>{{ classroom }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div v-else>
            {{ lesson.classrooms }}
          </div>
        </div>
        <div v-if="index + 1 !== timetable.length">
          <hr />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, PropType, ref } from "vue";
import { APITimetableDay } from "@/api/services/timetable";
import { getDayName, renderTime } from "@/utils/date";
import { APISubject } from "@/api/services/subjects";

interface TimetableData {
  subject: APISubject;
  classrooms: string[] | string;
  n: number;
  start: string;
  end: string;
  id: number;
}

const timetable = ref<TimetableData[]>([]);

const processTimetable = () => {
  const day = props.day;

  timetable.value = day.lessons.map((l) => ({
    classrooms: l.classroom.match(/((.+-.+)(\||,))*(.+-.+)/)
      ? l.classroom.split(/,|\|/).map((l) => l.trim())
      : l.classroom,
    ...l,
  }));
};

onMounted(() => {
  processTimetable();
});

const props = defineProps({
  day: {
    type: Object as PropType<APITimetableDay>,
    required: true,
  },
  isToday: {
    type: Boolean,
    default: false,
  },
  isTomorrow: {
    type: Boolean,
    default: false,
  },
});
</script>

<style scoped>
.card:hover,
div.alert:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition-duration: 0.5s;
}

.subject-icon {
  width: 40px;
}

.subject-icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}

h4 {
  font-weight: bold;
}

.subject-name {
  font-size: 1.1rem;
}

.classrooms-table > tbody > tr:last-child td {
  border-bottom: none !important;
}
</style>
