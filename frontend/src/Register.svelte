<script>
    let username = "";
    let email = "";
    let password = "";
    let error = "";

    async function handleRegister() {
        try {
            const res = await fetch("/api/register", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, email, password }),
            });

            if (res.ok) {
                window.location.hash = "login";
            } else {
                const data = await res.json();
                error = data.error || "Registration failed";
                alert(error);
            }
        } catch (e) {
            alert("An error occurred");
        }
    }
</script>

<div class="max-w-md mx-auto bg-white rounded-lg shadow overflow-hidden">
    <div class="px-6 py-8">
        <h2 class="text-2xl font-bold text-center text-gray-800 mb-8">
            Register
        </h2>
        <form on:submit|preventDefault={handleRegister}>
            <div class="mb-4">
                <label
                    class="block text-gray-700 text-sm font-bold mb-2"
                    for="username">Username</label
                >
                <input
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="username"
                    type="text"
                    bind:value={username}
                />
            </div>
            <div class="mb-4">
                <label
                    class="block text-gray-700 text-sm font-bold mb-2"
                    for="email">Email</label
                >
                <input
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="email"
                    type="email"
                    bind:value={email}
                />
            </div>
            <div class="mb-6">
                <label
                    class="block text-gray-700 text-sm font-bold mb-2"
                    for="password">Password</label
                >
                <input
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    id="password"
                    type="password"
                    bind:value={password}
                />
            </div>
            <button
                class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full transform transition hover:scale-105 duration-300 ease-in-out"
                type="submit"
            >
                Create Account
            </button>
        </form>
        <div class="mt-4 text-center">
            <p class="text-sm text-gray-600">
                Already have an account? <a
                    href="#login"
                    class="text-blue-600 hover:underline">Login</a
                >
            </p>
        </div>
    </div>
</div>
