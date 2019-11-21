import React, {useContext} from 'react';
import QuackContext from "../../context";

const QuackSadBasket = () => {
    const {state} = useContext(QuackContext);

    return (
        <svg
            xmlns="http://www.w3.org/2000/svg"
            width="122"
            height="65"
            viewBox="0 0 122 65"
        >
            <g fill="none" fillRule="evenodd" stroke="none" strokeWidth="1">
                <g transform="translate(-418 -758) translate(418 758) matrix(-1 0 0 1 122 0)">
                    <rect
                        width="122"
                        height="40.907"
                        x="0"
                        y="0"
                        fill="#4A90E2"
                        rx="20.454"
                    ></rect>
                    <path
                        fill="#4A90E2"
                        d="M55 6v7.083h53.451a33.844 33.844 0 014.549 17c0 18.778-15.222 34-34 34s-34-15.222-34-34C45 20.673 48.823 12.156 55 6z"
                    ></path>
                    <circle cx="79.5" cy="31.5" r="26.5" fill="#FFC9CF"></circle>
                </g>


                <text
                    fill="#000"
                    fontFamily="Monospace"
                    fontSize="30"
                    fontWeight="400"
                    transform="translate(-418 -758) translate(418 758)"
                >
                    <tspan x="25" y="41">
                        {state.sad.length.toString().padStart(2, '0')}
                    </tspan>
                </text>
                <g>
                    <g transform="translate(-418 -758) translate(418 758) translate(84 6)">
                        <circle cx="14.5" cy="14.5" r="14.5" fill="#F8E71C"></circle>
                        <path
                            fill="#FF6F2E"
                            d="M15.1 14.844c.725-.579.801 1.354 2.377 2.276 1.051.615 2.47 2.12 4.255 4.514L15.1 19.016a29.722 29.722 0 01-.092-.476h-1.129c-.028.154-.06.313-.092.476L7.305 21.91c1.686-2.578 3.054-4.175 4.105-4.79 1.576-.922 1.652-2.855 2.377-2.276.1.08.18.203.238.369h.837a.797.797 0 01.238-.37z"
                        ></path>
                        <ellipse
                            cx="14.975"
                            cy="18.779"
                            fill="#FF6F2E"
                            rx="1.189"
                            ry="1.664"
                        ></ellipse>
                        <path
                            fill="#F6560D"
                            d="M14.266 21.32c-1.18.176-2.066.16-2.659-.047-.641-.224-2.075-.012-4.302.637l7.262-3.369 7.165 3.093c-2.162-.465-3.563-.585-4.205-.36-.641.223-1.628.223-2.96 0z"
                        ></path>
                        <circle cx="10.221" cy="11.172" r="1.664" fill="#000"></circle>
                        <circle cx="18.779" cy="11.172" r="1.664" fill="#000"></circle>
                        <path
                            fill="#000"
                            d="M18.066 5.23a2.615 2.615 0 003.988 1.98l.603.745a3.566 3.566 0 01-5.542-2.724z"
                        ></path>
                        <path
                            fill="#000"
                            d="M7.607 5.23a2.615 2.615 0 003.989 1.98l.602.745A3.566 3.566 0 016.656 5.23z"
                            transform="matrix(-1 0 0 1 18.855 0)"
                        ></path>
                    </g>
                    <path
                        fill="#4A90E2"
                        d="M20.5 17c.828 0 1.5-.596 1.5-1.33 0-.735-.786-2.67-1.615-2.67C19.557 13 19 14.935 19 15.67c0 .734.672 1.33 1.5 1.33z"
                        transform="translate(-418 -758) translate(418 758) translate(84 6)"
                    ></path>
                </g>
            </g>
        </svg>

    );
};

export default QuackSadBasket;