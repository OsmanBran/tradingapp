import React from 'react';
import { Dot, DotProps } from 'recharts';

interface CustomDotProps extends DotProps {
    index: number;
    intersections: number[];
}

const CustomDot: React.FC<CustomDotProps> = ({ cx, cy, index, intersections }) => {
    if (intersections.includes(index)) {
        return <Dot cx={cx} cy={cy} r={5} fill="red" />;
    }

    return null; // Return null for non-intersection points to keep them hidden
};

export default CustomDot;