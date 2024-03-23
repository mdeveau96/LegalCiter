<script setup>
import { RouterView } from 'vue-router'
import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'

</script>

<template>
  <div>
    <header class="border shadow relative">
      <NavBar />
    </header>
    <div class="inline-flex bg-gray-100 dark:bg-slate-800 border-r-2 w-64 px-2 h-screen justify-center">
      <SideBar />
    </div>
    <RouterView />
  </div>
</template>
