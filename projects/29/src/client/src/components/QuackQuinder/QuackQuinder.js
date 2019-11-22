import React, {useContext, useState, useEffect} from 'react';
import QuackContext from '../../context';
import styled from 'styled-components';
import {useSprings, animated, interpolate} from 'react-spring'
import {useGesture} from 'react-use-gesture';

import {useDrag} from 'react-use-gesture'
import {QuackCard} from "../QuackCard";
import testdata from "../../testdata/testdata";
import axios from "axios";
import {v4 as uuidv4} from "uuid";



const Outer = styled(animated.div)`
  position: absolute;

  will-change: transform;
  display: flex;
  align-items: center;
  justify-content: center;
`
const Inner = styled(animated.div)`
    background-color: white;
  background-size: auto 85%;
  background-repeat: no-repeat;
  background-position: center center;
  width: 45vh;
  max-width: 300px;
  height: 85vh;
  max-height: 570px;
  will-change: transform;
  border-radius: 10px;
  box-shadow: 0 12.5px 100px -10px rgba(50, 50, 73, 0.4), 0 10px 10px -10px rgba(50, 50, 73, 0.3);
`

const to = i => ({x: 0, y: i * -4, scale: 1, rot: -5 + Math.random() * 10, delay: i * 100})
const from = i => ({x: 0, rot: 0, scale: 1.5, y: -1000})
// This is being used down there in the view, it interpolates rotation and scale into a css transform
const trans = (r, s) => `perspective(1500px) rotateX(5deg) rotateY(${r / 10}deg) rotateZ(${r}deg) scale(${s})`

function QuackQuinder({results}) {
    const {state, dispatch} = useContext(QuackContext);
    const {happy, sad} = state;
    const [gone] = useState(() => new Set()) // The set flags all the results that are flicked out
    const [props, set] = useSprings(results.length, i => ({...to(i), from: from(i)})) // Create a bunch of springs using the helpers above
    // Create a gesture, we're interested in down-state, delta (current-pos - click-pos), direction and velocity
    const bind = useDrag(({args: [index], down, movement: [mx], distance, direction: [xDir], velocity}) => {
        const trigger = velocity > 0.2 // If you flick hard enough it should trigger the card to fly out
        const dir = xDir < 0 ? -1 : xDir > 0 ? 1 : 0 // Direction should either point left or right

        if (down) dispatch({type: 'SET_VOTESTATE', data: dir})
        if (!down) dispatch({type: 'SET_VOTESTATE', data: 0})

        if (!down && trigger) {
            gone.add(index)
            if (dir == 1) {
                dispatch({type: 'ADD_HAPPY', data: results[index]})
            } else {
                dispatch({type: 'ADD_SAD', data: results[index]})
            }

        }
        set(i => {
            if (index !== i) return // We're only interested in changing spring-data for the current spring

            const isGone = gone.has(index)
            const x = isGone ? (200 + window.innerWidth) * dir : down ? mx : 0 // When a card is gone it flys out left or right, otherwise goes back to zero
            const rot = mx / 100 + (isGone ? dir * 10 * velocity : 0) // How much the card tilts, flicking it harder makes it rotate faster
            const scale = down ? 1.1 : 1 // Active results lift up a bit
            return {x, rot, scale, delay: undefined, config: {friction: 50, tension: down ? 800 : isGone ? 200 : 500}}
        })
        //if (!down && gone.size === results.length) setTimeout(() => gone.clear() || set(i => to(i)), 600)
    })

    // Now we're just mapping the animated values to our view, that's it. Btw, this component only renders once. :-)
    return props.map(({x, y, rot, scale}, i) => (
        <animated.div id={i} className={"outerCard"} key={i}
                      style={{transform: interpolate([x, y], (x, y) => `translate3d(${x}px,${y}px,0)`)}}>
            {/* This is the card itself, we're binding our gesture to it (and inject its index so we know which is which) */}
            <animated.div className={"innerCard"} {...bind(i)} style={{transform: interpolate([rot, scale], trans)}}>
                <QuackCard data={results[i]}/>
            </animated.div>
        </animated.div>
    ))
}


export default QuackQuinder;