import Link from "next/link";
import { useRouter } from "next/router";

export default function NavBar() {
    const router = useRouter();
    return (
        <nav>
            <Link className={`link ${router.pathname === "/" ? "active" : ""}`} href="/">
                Home
            </Link>
            <Link className={`link ${router.pathname === "/about" ? "active" : ""}`} href="/about">
                About
            </Link>
            <style jsx>{`
                .link {
                    text-decoration: none;
                }

                nav {
                    background-color: tomato;
                    /* padding: 30px; */
                }
                .active {
                    color: tomato;
                }
            `}</style>
        </nav>
    );
}
