<script setup lang="ts">
import { object, string, type InferType } from 'yup'
import type { FormSubmitEvent } from '#ui/types'

const schema = object({
    title: string().required('Required'),
    caseName: string().required('Required'),
    caseText: string().required('Required')
})

type Schema = InferType<typeof schema>

const state = reactive({
    title: undefined,
    caseName: undefined,
    caseText: undefined,
})

async function onSubmit(event: FormSubmitEvent<Schema>) {
    // Do something with event.data
    console.log(event.data)
}
</script>

<template>
    <UForm :schema="schema" :state="state" class="space-y-4" @submit="onSubmit">
        <UFormGroup label="Title" name="title">
            <UInput v-model="state.title" placeholder="Case Title..."/>
        </UFormGroup>

        <UFormGroup label="Case" name="caseName">
            <UInput v-model="state.caseName" type="text" placeholder="Case Name..."/>
        </UFormGroup>

        <UFormGroup label="Cite Text" name="casetext">
            <UTextarea v-model="state.caseText" placeholder="Cite Text..."/>
        </UFormGroup>

        <UButton type="submit">
            Submit
        </UButton>
    </UForm>
</template>
