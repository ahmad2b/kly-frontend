import React from "react";
import Image from "next/image";
import Link from "next/link";
import { Button } from "./ui/button";

function Navbar() {
  return (
    <div className="hidden md:block">
      <div className="p-6 flex justify-between">
        <div>
          <Image src={"/logo.svg"} alt="Logo" width={40} height={40} />
        </div>
        <div className="flex gap-4">
          <Link href="/log-in">
            <Button
              variant="secondary"
              className="bg-gray-800 text-white hover:bg-gray-700"
            >
              Log In
            </Button>
          </Link>
          
        
          <Link href="/sign-up">
            <Button
              variant="secondary"
              className="hover:bg-gray-200"
            >
              Sign Up
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default Navbar;
