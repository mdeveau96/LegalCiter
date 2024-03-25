<script setup lang="ts">
const items = [{
    slot: 'create-cite',
    label: 'Create Cite'
}, {
    slot: 'your-cites',
    label: 'Your Cites'
}]

const route = useRoute()
const router = useRouter()

const selected = computed({
    get() {
        const index = items.findIndex((item) => item.label === route.query.tab)
        if (index === -1) {
            return 0
        }

        return index
    },
    set(value) {
        // Hash is specified here to prevent the page from scrolling to the top
        router.replace({ query: { tab: items[value].label }, hash: '#control-the-selected-index' })
    }
})
</script>

<template>
    <UTabs v-model="selected" :items="items" :default-index="0" class="mx-72 pt-2">
        <template #create-cite="{ item }">
            <UCard>
                <CreateCite />
            </UCard>
        </template>
        <template #your-cites="{ item }">
            <UCard>
                <YourCite />
            </UCard>
        </template>
    </UTabs>

</template>
