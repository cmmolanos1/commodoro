import { ResponsiveRadar } from '@nivo/radar';
import React from 'react';

// make sure parent container have a defined height when using
// responsive component, otherwise height will be 0 and
// no chart will be rendered.
// website examples showcase many properties,
// you'll often use just a few of them.

const SkillRadar = ({ data }) => {
  return (
    <ResponsiveRadar
        data={data}
        keys={[ 'percentage' ]}
        indexBy="title"
        maxValue="auto"
        margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
        curve="linearClosed"
        borderWidth={2}
        borderColor={{ from: 'color', modifiers: [] }}
        gridLevels={4}
        gridShape="circular"
        gridLabelOffset={12}
        enableDots={true}
        dotSize={6}
        dotColor={{ from: 'color', modifiers: [] }}
        dotBorderWidth={2}
        dotBorderColor={{ from: 'color' }}
        enableDotLabel={true}
        dotLabel="value"
        dotLabelYOffset={-12}
        colors={{ scheme: 'dark2' }}
        fillOpacity={0.25}
        blendMode="multiply"
        animate={true}
        motionStiffness={90}
        motionDamping={15}
        isInteractive={true}
        legends={[
            {
                anchor: 'top-left',
                direction: 'column',
                translateX: -50,
                translateY: -40,
                itemWidth: 80,
                itemHeight: 20,
                itemTextColor: '#999',
                symbolSize: 12,
                symbolShape: 'circle',
                effects: [
                    {
                        on: 'hover',
                        style: {
                            itemTextColor: '#000'
                        }
                    }
                ]
            }
        ]}
    /> 
  )
}
export default SkillRadar;