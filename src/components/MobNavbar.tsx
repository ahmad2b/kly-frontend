import React from "react";
import { AlignRight } from "lucide-react";
import Image from "next/image";

function MobNavbar() {
  return (
    <div className="block md:hidden p-4">
      <div className="flex justify-between">
        <div>
          <Image src={"/logo.svg"} alt="Logo" width={40} height={40} />
        </div>
        <div>
          <AlignRight />
        </div>
      </div>
    </div>
  );
}

export default MobNavbar;
