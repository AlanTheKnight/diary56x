<template>
  <div v-if="isAuthenticated" class="rt-wp mt-4 container">
    <div class="row" v-if="isStudent(user)">
      <card
        icon="timetable"
        title="Расписание"
        v-if="pluginEnabled(user, 'timetable')"
        link="/timetable"
      />
      <card
        icon="homework"
        title="Домашнее задание"
        v-if="pluginEnabled(user, 'homework')"
        link="/"
      />
      <card
        icon="notes"
        title="Конспекты"
        v-if="pluginEnabled(user, 'notes')"
        link="/"
      />
    </div>
    <div class="row" v-if="isAdmin(user)">
      <card icon="admin" title="Панель администратора" link="/admin" />
    </div>
  </div>
  <div v-else>
    <landing />
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";

import Landing from "./components/Landing.vue";
import Card from "./components/Card.vue";

import { key } from "@/store";
import { useStore } from "vuex";

import {
  APIUser,
  isStudent,
  pluginEnabled,
  isAdmin,
} from "@/api/services/auth";

export default defineComponent({
  name: "Home",
  components: {
    Landing,
    Card,
  },
  setup() {
    const store = useStore(key);

    const isAuthenticated = computed(() => store.getters["isAuthenticated"]);
    const user = computed(() => store.state.user as APIUser);

    return { isAuthenticated, pluginEnabled, user, isStudent, isAdmin };
  },
});
</script>

<style scoped></style>
