<script setup lang="ts">
const route = useRoute()
const colorMode = useColorMode()
const isDark = computed({
  get() {
    return colorMode.value === 'dark'
  },
  set() {
    colorMode.preference = colorMode.value === 'dark' ? 'light' : 'dark'
  }
})

const links = [
  [{
    label: 'About',
    to: '/about'
  }], [{
    label: 'Log In',
    to: '/login'
  }]
]
</script>

<template>
  <UContainer class="flex sticky top-0 z-40 bg-white dark:bg-gray-900 max-w-full">
    <NuxtLink to="/" class="flex pr-8">
      <img src="/law-firm-icon-13.png" class="h-8 w-9 mt-2">
      <h1 class="font-sans font-bold text-2xl py-1.5 px-2 text-legal-950 dark:text-white">LegalCiter</h1>
    </NuxtLink>
    <UDivider orientation="vertical" size="2xs" class="w-auto py-2 ml-2" />
    <UHorizontalNavigation :links="links" class="pl-1.5">
      <template #default="{ link }" class="bg-gray-100">
        <span class="group-hover:text-legal-800 group-hover:bg-transparent relative dark:text-white">{{ link.label }}</span>
      </template>
    </UHorizontalNavigation>
    <UButton square
      class="hover:bg-transparent dark:hover:bg-transparent hover:text-legal-500 dark:hover:text-legal-500 text-legal-800 dark:text-legal-800"
      color="legal" label="Sign Up" variant="ghost" to="/signup" />
    <UDivider orientation="vertical" size="2xs" class="w-auto py-2 ml-2" />
    <ClientOnly>
      <UButton :icon="isDark ? 'i-heroicons-moon-20-solid' : 'i-heroicons-sun-20-solid'" color="gray" variant="ghost"
        aria-label="Theme" @click="isDark = !isDark" class="px-3 hover:bg-transparent dark:hover:bg-transparent" />
      <template #fallback>
        <div class="w-8 h-8" />
      </template>
    </ClientOnly>
  </UContainer>
  <UDivider />
</template>