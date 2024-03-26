export default defineAppConfig({
    ui: {
        primary: "blue",
        colors: ["legal"],
        tabs:{
            list: { 
                background: 'bg-gray-100 dark:bg-neutral-800',
                marker: {
                    background: 'bg-white dark:bg-black',
                },
                tab: { 
                    background: 'focus:bg-white dark:focus:bg-black' 
                }
            }
        },
        card:{
            background: 'bg-white dark:bg-neutral-800',
            ring: 'ring-gray-200 dark:ring-neutral-700'
        },
        input:{
            color: {
                white: {
                    outline: 'shadow-sm bg-white dark:bg-black text-gray-900 dark:text-white ring-1 ring-inset ring-gray-200 dark:ring-neutral-700 focus:ring-2 focus:ring-primary-500 dark:focus:ring-primary-400',
                },
            }
        },
        divider: {
            border: {
                base: 'flex border-gray-200 dark:border-neutral-700',
            }
        },
        textarea: {
            color: {
                white: {
                    outline: 'shadow-sm bg-white dark:bg-black text-gray-900 dark:text-white ring-1 ring-inset ring-gray-200 dark:ring-neutral-700 focus:ring-2 focus:ring-primary-500 dark:focus:ring-primary-400',
                },
            }
        },
        modal: {
            overlay: {
                background: 'bg-gray-200/75 dark:bg-neutral-800/75',
            },
            background: 'bg-white dark:bg-black',
        }
    }
})
  