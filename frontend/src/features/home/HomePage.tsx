import { Link } from "react-router-dom";
import StateDemo from "../state-demo/StateDemo";

export default function HomePage() {
    return (
        <main className="min-h-screen bg-slate-50 p-8 text-slate-900">
            <div className="mx-auto max-w-3xl space-y-4">
                <p className="text-sm font-semibold uppercase tracking-widest text-indigo-600">
                    Przykład
                </p>

                <h1 className="text-3xl font-bold">Strona główna</h1>

                <p className="text-slate-600">
                    Nie wygląda, ale jest! Zmień mnie, gdy przyjdzie czas na tworzenie strony od zera.
                </p>

                <Link to="/dummy"
                    className="inline-block rounded-lg bg-indigo-600 px-4 py-2 font-medium text-white hover:bg-indigo-700"
                >
                    Do dummy
                </Link>

      <StateDemo />
            </div>
        </main>
    )
}
