<script>
    let step = 1;
    let achievement_1 = "";
    let achievement_2 = "";
    let achievement_3 = "";

    function nextStep() {
        if (validateStep(step)) {
            step += 1;
        }
    }

    function prevStep() {
        if (step > 1) {
            step -= 1;
        }
    }

    function validateStep(s) {
        if (s === 1 && !achievement_1.trim()) return false;
        if (s === 2 && !achievement_2.trim()) return false;
        return true;
    }

    async function submitReflection() {
        if (!achievement_3.trim()) return;

        try {
            const res = await fetch("/api/reflect", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    achievement_1,
                    achievement_2,
                    achievement_3,
                }),
            });

            if (res.ok) {
                window.location.hash = "dashboard";
            } else {
                alert("Failed to save reflection");
            }
        } catch (e) {
            console.error(e);
            alert("Error saving reflection");
        }
    }
</script>

<div class="max-w-2xl mx-auto bg-white shadow sm:rounded-lg overflow-hidden">
    <div class="px-4 py-5 sm:p-6">
        <div class="w-full bg-gray-200 rounded-full h-2.5 mb-6">
            <div
                class="bg-blue-600 h-2.5 rounded-full"
                style="width: {((step - 1) / 2) * 100}%"
            ></div>
        </div>

        <form on:submit|preventDefault={submitReflection}>
            {#if step === 1}
                <div class="space-y-4 animate-fade-in">
                    <label
                        for="a1"
                        class="block text-xl font-medium text-gray-900 text-center"
                        >What's one thing you managed well today?</label
                    >
                    <div class="mt-1">
                        <textarea
                            id="a1"
                            rows="4"
                            class="shadow-sm focus:ring-blue-500 focus:border-blue-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md p-3"
                            bind:value={achievement_1}
                            placeholder="I completed that task I was dreading..."
                        ></textarea>
                    </div>
                    <button
                        type="button"
                        on:click={nextStep}
                        class="w-full inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none disabled:opacity-50"
                        disabled={!achievement_1.trim()}
                    >
                        Next
                    </button>
                </div>
            {:else if step === 2}
                <div class="space-y-4 animate-fade-in">
                    <label
                        for="a2"
                        class="block text-xl font-medium text-gray-900 text-center"
                        >What's another achievement from today?</label
                    >
                    <div class="mt-1">
                        <textarea
                            id="a2"
                            rows="4"
                            class="shadow-sm focus:ring-blue-500 focus:border-blue-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md p-3"
                            bind:value={achievement_2}
                            placeholder="I helped a colleague..."
                        ></textarea>
                    </div>
                    <div class="flex justify-between space-x-4">
                        <button
                            type="button"
                            on:click={prevStep}
                            class="inline-flex justify-center py-2 px-4 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none"
                        >
                            Previous
                        </button>
                        <button
                            type="button"
                            on:click={nextStep}
                            class="flex-1 inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none disabled:opacity-50"
                            disabled={!achievement_2.trim()}
                        >
                            Next
                        </button>
                    </div>
                </div>
            {:else if step === 3}
                <div class="space-y-4 animate-fade-in">
                    <label
                        for="a3"
                        class="block text-xl font-medium text-gray-900 text-center"
                        >Share one final achievement from today:</label
                    >
                    <div class="mt-1">
                        <textarea
                            id="a3"
                            rows="4"
                            class="shadow-sm focus:ring-blue-500 focus:border-blue-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md p-3"
                            bind:value={achievement_3}
                            placeholder="I went for a walk..."
                        ></textarea>
                    </div>
                    <div class="flex justify-between space-x-4">
                        <button
                            type="button"
                            on:click={prevStep}
                            class="inline-flex justify-center py-2 px-4 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none"
                        >
                            Previous
                        </button>
                        <button
                            type="submit"
                            class="flex-1 inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none disabled:opacity-50"
                            disabled={!achievement_3.trim()}
                        >
                            Complete
                        </button>
                    </div>
                </div>
            {/if}
        </form>
    </div>
</div>

<style>
    .animate-fade-in {
        animation: fadeIn 0.3s ease-in-out;
    }
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
