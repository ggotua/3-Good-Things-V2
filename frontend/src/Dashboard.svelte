<script>
    import { onMount } from "svelte";
    // export let navigate; // Received from parent but simplistic routing uses hash

    // Mock data
    let user = null;
    let today_reflection = null;
    let recent_reflections = [];
    let loading = true;

    onMount(async () => {
        try {
            const res = await fetch("/api/dashboard");
            if (res.ok) {
                const data = await res.json();
                user = data.user;
                today_reflection = data.today_reflection;
                recent_reflections = data.recent_reflections;
            } else {
                // Redirect to login if unauthorized
                if (res.status === 401) window.location.hash = "login";
            }
        } catch (e) {
            console.error(e);
        } finally {
            loading = false;
        }
    });
</script>

<div class="space-y-6">
    <div class="bg-white shadow px-4 py-5 sm:rounded-lg sm:p-6">
        <div class="md:grid md:grid-cols-3 md:gap-6">
            <div class="md:col-span-1">
                <h3 class="text-lg font-medium leading-6 text-gray-900">
                    Welcome back, {user ? user.username : "User"}!
                </h3>
                <p class="mt-1 text-sm text-gray-500">
                    {#if !today_reflection}
                        Ready for today's reflection? Take a moment to
                        acknowledge your achievements.
                    {/if}
                </p>
            </div>
            <div class="mt-5 md:mt-0 md:col-span-2">
                {#if !today_reflection}
                    <div class="rounded-md bg-blue-50 p-4">
                        <div class="flex">
                            <div class="flex-shrink-0">
                                <!-- Heroicon name: solid/information-circle -->
                                <svg
                                    class="h-5 w-5 text-blue-400"
                                    xmlns="http://www.w3.org/2000/svg"
                                    viewBox="0 0 20 20"
                                    fill="currentColor"
                                    aria-hidden="true"
                                >
                                    <path
                                        fill-rule="evenodd"
                                        d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                                        clip-rule="evenodd"
                                    />
                                </svg>
                            </div>
                            <div class="ml-3 flex-1 md:flex md:justify-between">
                                <p class="text-sm text-blue-700">
                                    You haven't logged your achievements for
                                    today yet.
                                </p>
                                <p class="mt-3 text-sm md:mt-0 md:ml-6">
                                    <button
                                        on:click={() =>
                                            (window.location.hash = "reflect")}
                                        class="whitespace-nowrap font-medium text-blue-700 hover:text-blue-600"
                                        >Start Reflection <span
                                            aria-hidden="true">&rarr;</span
                                        ></button
                                    >
                                </p>
                            </div>
                        </div>
                    </div>
                {:else}
                    <div class="bg-green-50 overflow-hidden sm:rounded-lg">
                        <div class="px-4 py-3 sm:px-6 bg-green-100">
                            <h3
                                class="text-lg leading-6 font-medium text-green-900"
                            >
                                Today's Achievements
                            </h3>
                        </div>
                        <div class="border-t border-green-200 px-4 py-3 sm:p-0">
                            <ul class="divide-y divide-green-200">
                                <li class="py-3 px-4 text-sm text-green-900">
                                    {today_reflection.achievement_1}
                                </li>
                                <li class="py-3 px-4 text-sm text-green-900">
                                    {today_reflection.achievement_2}
                                </li>
                                <li class="py-3 px-4 text-sm text-green-900">
                                    {today_reflection.achievement_3}
                                </li>
                            </ul>
                        </div>
                        <div class="px-4 py-3 bg-green-50 text-right sm:px-6">
                            <button
                                on:click={() =>
                                    (window.location.hash = "reflect")}
                                class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
                            >
                                Edit
                            </button>
                        </div>
                    </div>
                {/if}
            </div>
        </div>
    </div>

    <div class="bg-white shadow sm:rounded-lg">
        <div class="px-4 py-5 sm:px-6">
            <h3 class="text-lg leading-6 font-medium text-gray-900">
                Recent Reflections
            </h3>
        </div>
        <div class="border-t border-gray-200">
            {#if recent_reflections.length > 0}
                <ul class="divide-y divide-gray-200">
                    {#each recent_reflections as reflection}
                        <li class="px-4 py-4 sm:px-6">
                            <div class="flex items-center justify-between">
                                <p
                                    class="text-sm font-medium text-blue-600 truncate"
                                >
                                    {reflection.date}
                                </p>
                                <div class="ml-2 flex-shrink-0 flex">
                                    <!-- Edit button or status -->
                                </div>
                            </div>
                            <div class="mt-2 sm:flex sm:justify-between">
                                <div class="sm:flex">
                                    <ul
                                        class="list-disc pl-5 text-sm text-gray-500"
                                    >
                                        <li>{reflection.achievement_1}</li>
                                        <li>{reflection.achievement_2}</li>
                                        <li>{reflection.achievement_3}</li>
                                    </ul>
                                </div>
                            </div>
                        </li>
                    {/each}
                </ul>
            {:else}
                <div class="px-4 py-5 sm:p-6 text-center text-gray-500">
                    No past reflections found.
                </div>
            {/if}
        </div>
    </div>
</div>
