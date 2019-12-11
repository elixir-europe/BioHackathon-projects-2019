import React, {useContext} from 'react';
import QuackContext from "../../context";
import {v4 as uuidv4} from 'uuid';


const QuackBasket = () => {
    const {state} = useContext(QuackContext);

    return (
        <div className={"dropdown"}>
            <svg width="122" height="65" viewBox="0 0 122 65">
                <g fill="none" fillRule="evenodd" stroke="none" strokeWidth="1">
                    <g transform="translate(-417 -660) translate(417 660)">
                        <rect
                            width="122"
                            height="40.907"
                            x="0"
                            y="0"
                            fill="#4A90E2"
                            rx="20.454"
                        ></rect>
                        <g transform="translate(9 3)">
                            <circle cx="14.5" cy="17.5" r="14.5" fill="#F8E71C"></circle>
                            <path
                                fill="#000"
                                d="M3.492 0c1.855 0 3.372 1.324 3.493 3H0c.12-1.676 1.638-3 3.492-3z"
                                transform="translate(6 12)"
                            ></path>
                            <path
                                fill="#F8E71C"
                                d="M3.49.857c1.338 0 2.437.941 2.556 2.142H.933C1.052 1.8 2.151.857 3.49.857z"
                                transform="translate(6 12)"
                            ></path>
                            <path
                                fill="#000"
                                d="M3.492 0c1.855 0 3.372 1.324 3.493 3H0c.12-1.676 1.638-3 3.492-3z"
                                transform="translate(16 12)"
                            ></path>
                            <path
                                fill="#F8E71C"
                                d="M3.49.857c1.338 0 2.437.941 2.556 2.142H.933C1.052 1.8 2.151.857 3.49.857z"
                                transform="translate(16 12)"
                            ></path>
                            <path
                                fill="#FF6F2E"
                                d="M7 20c1.915.726 3.375.802 4.38.227 1.507-.862 1.58-2.669 2.273-2.128.463.36.463 1.661 0 3.901L7 20z"
                            ></path>
                            <path
                                fill="#FF6F2E"
                                d="M15 20c1.991.726 3.475.802 4.452.227 1.466-.862 1.537-2.669 2.21-2.128.45.36.45 1.661 0 3.901L15 20z"
                                transform="matrix(-1 0 0 1 37 0)"
                            ></path>
                            <path
                                fill="#FF6F2E"
                                stroke="#FF6F2E"
                                strokeLinejoin="round"
                                d="M16 18v3h-2v-3h2z"
                            ></path>
                            <ellipse cx="13.5" cy="22" fill="#A2FDC8" rx="1.5" ry="1"></ellipse>
                            <path
                                fill="#F6560D"
                                d="M14 20c2.32 3 3.768 4.61 4.343 4.833.576.223 1.462.223 2.657 0v-2.71L14 20z"
                                transform="matrix(-1 0 0 1 35 0)"
                            ></path>
                            <path
                                fill="#F6560D"
                                d="M7 20c2.26 3 3.686 4.61 4.276 4.833.59.223 1.498.223 2.724 0v-2.71L7 20z"
                            ></path>
                        </g>
                        <path
                            fill="#4A90E2"
                            d="M55 6v7.083h53.451a33.844 33.844 0 014.549 17c0 18.778-15.222 34-34 34s-34-15.222-34-34C45 20.673 48.823 12.156 55 6z"
                        ></path>
                        <circle cx="79.5" cy="31.5" r="26.5" fill="#A2FDC8"></circle>
                    </g>
                    <text
                        fill="#000"
                        fontFamily="Monospace"
                        fontSize="30"
                        fontWeight="400"
                        transform="translate(-417 -660) translate(417 660)"
                    >
                        <tspan x="62" y="41">
                            {state.happy.length.toString().padStart(2, '0')}
                        </tspan>
                    </text>
                </g>
            </svg>
            <div className="dropdown-content">
                {state.happy.map((ele)=>{
                    return <a key={uuidv4()} target='_blank' href={ele.seeAlso}>{ele.title}</a>
                })}

            </div>
        </div>
    );
};

export default QuackBasket;