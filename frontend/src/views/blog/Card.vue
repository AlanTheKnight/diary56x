<template>
  <div class="card card-body" :class="{ 'mb-3': !noMargin }">
    <router-link :to="'/blog/' + blogPost.slug" class="stretched-link" />
    <li class="row align-items-center">
      <div class="col">
        <div>
          <h5 class="mt-0">{{ blogPost.title }}</h5>
        </div>
        <p class="text-muted my-0">{{ author }}, {{ postDate }}</p>
      </div>

      <div class="col-auto">
        <div class="w-100">
          <img
            :src="postImage"
            class="mr-3 post-image"
            alt=""
            height="70"
            width="70"
          />
        </div>
      </div>
    </li>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, PropType } from "vue";
import { APIPost, postAuthor } from "@/api/services/blog";
import { toShortDate } from "@/utils/date";
import { getImage } from "@/utils/blog";

export default defineComponent({
  setup(props) {
    const processDate = () => {
      return toShortDate(new Date(props.blogPost.date));
    };

    return {
      postImage: computed(() => getImage(props.blogPost, true) as string),
      postDate: computed(() => processDate()),
      author: computed(() => postAuthor(props.blogPost)),
    };
  },
  props: {
    blogPost: {
      type: Object as PropType<APIPost>,
      required: true,
    },
    noMargin: {
      type: Boolean,
      default: false,
    },
  },
});
</script>

<style></style>
