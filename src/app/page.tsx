"use client";
import { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import cytoscape from 'cytoscape';

type Graph = {
  [key: string]: { [key: string]: number };
};

type DijkstraResult = {
  distances: { [key: string]: number };
  path: { [key: string]: string | null };
};

export default function Home() {
  const [graph, setGraph] = useState<Graph>({
    A: { B: 1, C: 4 },
    B: { A: 1, C: 2, D: 5 },
    C: { A: 4, B: 2, D: 1 },
    D: { B: 5, C: 1 },
  });
  const [startNode, setStartNode] = useState<string>('A');
  const [result, setResult] = useState<DijkstraResult | null>(null);

  const cyRef = useRef<HTMLDivElement>(null);

  const handleDijkstra = async () => {
    try {
      const response = await axios.post('/api/dijkstra', {
        graph,
        start: startNode,
      });
      setResult(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
    if (cyRef.current) {
      const elements = Object.entries(graph).flatMap(([source, edges]) =>
        Object.entries(edges).map(([target, weight]) => ({
          data: { id: source + target, source, target, weight }
        }))
      );

      const nodes = Object.keys(graph).map((node) => ({
        data: { id: node }
      }));

      const cy = cytoscape({
        container: cyRef.current,
        elements: [...nodes, ...elements],
        style: [
          {
            selector: 'node',
            style: {
              'background-color': '#007bff',
              label: 'data(id)'
            }
          },
          {
            selector: 'edge',
            style: {
              'width': 2,
              'line-color': '#ccc',
              'target-arrow-color': '#ccc',
              'target-arrow-shape': 'triangle',
              label: 'data(weight)'
            }
          }
        ],
        layout: {
          name: 'grid',
          rows: Math.ceil(Object.keys(graph).length / 3)
        }
      });

      return () => cy.destroy();
    }
  }, [graph]);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-6xl font-bold">Hello Pythons</h1>
      <p className="text-lg text-gray-600">
        This is a simple Dijkstra's algorithm implementation using Python and Next.js.
      </p>
      <h2 className="text-2xl">Graph:</h2>
      <div ref={cyRef} style={{ width: '100%', height: '600px', border: '1px solid #ccc' }}></div>

      <pre>{JSON.stringify(graph, null, 2)}</pre>
      <h2 className="text-2xl">Start Node:</h2>
      <input
        type="text"
        value={startNode}
        onChange={(e) => setStartNode(e.target.value)}
        className="border text-black border-gray-300 rounded px-2 py-1"
      />
    
      <button onClick={handleDijkstra} className="mt-6 px-4 py-2 bg-blue-500 text-white rounded">
        Run Dijkstra
      </button>
      {result && (
        <div className="mt-4">
          <h2 className="text-2xl">Result:</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </main>
  );
}
