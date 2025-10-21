import { useState, useEffect } from 'react'
import { TrendingUp, Hash, Users, BarChart2 } from 'lucide-react'
import { AreaChart, Area, BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar'
import CountUp from 'react-countup'
import 'react-circular-progressbar/dist/styles.css'

export default function Dashboard() {
  const [seoScore, setSeoScore] = useState(0)
  
  useEffect(() => {
    // Animate score on mount
    setTimeout(() => setSeoScore(87), 500)
  }, [])

  // Sample data
  const trafficData = [
    { month: 'Jan', organic: 4000, paid: 2400 },
    { month: 'Feb', organic: 5000, paid: 2800 },
    { month: 'Mar', organic: 6500, paid: 3200 },
    { month: 'Apr', organic: 8200, paid: 3800 },
    { month: 'May', organic: 11000, paid: 4200 },
    { month: 'Jun', organic: 14500, paid: 4800 },
  ]

  const stats = [
    { label: 'SEO Score', value: seoScore, suffix: '%', color: 'from-blue-500 to-cyan-500', icon: TrendingUp },
    { label: 'Total Keywords', value: 248, suffix: '', color: 'from-purple-500 to-pink-500', icon: Hash },
    { label: 'Organic Traffic', value: 14500, suffix: '', color: 'from-green-500 to-emerald-500', icon: Users },
    { label: 'Avg. Position', value: 4.2, suffix: '', color: 'from-orange-500 to-red-500', icon: BarChart2 },
  ]

  const keywordData = [
    { keyword: 'SEO Tools', position: 3, volume: 12000, difficulty: 68 },
    { keyword: 'AI Content', position: 5, volume: 8500, difficulty: 72 },
    { keyword: 'Website Audit', position: 2, volume: 15000, difficulty: 45 },
    { keyword: 'SEO Analysis', position: 7, volume: 9200, difficulty: 58 },
  ]

  return (
    <div className="space-y-6">
      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {stats.map((stat, index) => {
          const Icon = stat.icon
          return (
            <div
              key={index}
              className="bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-lg hover-lift"
              style={{ animationDelay: `${index * 0.1}s` }}
            >
              <div className="flex items-center justify-between mb-4">
                <div className={`w-12 h-12 bg-gradient-to-br ${stat.color} rounded-xl flex items-center justify-center`}>
                  <Icon className="w-6 h-6 text-white" />
                </div>
              </div>
              <p className="text-3xl font-bold text-gray-900 dark:text-white">
                <CountUp end={stat.value} duration={2} decimals={stat.label.includes('Position') ? 1 : 0} />
                {stat.suffix}
              </p>
              <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">{stat.label}</p>
            </div>
          )
        })}
      </div>

      {/* Charts Row */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Traffic Chart */}
        <div className="lg:col-span-2 bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-lg">
          <h3 className="text-xl font-bold mb-4 text-gray-900 dark:text-white">Traffic Overview</h3>
          <ResponsiveContainer width="100%" height={300}>
            <AreaChart data={trafficData}>
              <defs>
                <linearGradient id="colorOrganic" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.8}/>
                  <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
              <XAxis dataKey="month" stroke="#9ca3af" />
              <YAxis stroke="#9ca3af" />
              <Tooltip />
              <Area type="monotone" dataKey="organic" stroke="#3b82f6" fillOpacity={1} fill="url(#colorOrganic)" />
            </AreaChart>
          </ResponsiveContainer>
        </div>

        {/* SEO Score */}
        <div className="bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-lg">
          <h3 className="text-xl font-bold mb-4 text-gray-900 dark:text-white">SEO Health</h3>
          <div className="flex justify-center">
            <div style={{ width: 180, height: 180 }}>
              <CircularProgressbar
                value={seoScore}
                text={`${seoScore}%`}
                styles={buildStyles({
                  pathColor: `rgba(59, 130, 246, ${seoScore / 100})`,
                  textColor: '#3b82f6',
                  trailColor: '#e5e7eb',
                  pathTransitionDuration: 2,
                })}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Keywords Table */}
      <div className="bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-lg">
        <h3 className="text-xl font-bold mb-4 text-gray-900 dark:text-white">Top Keywords</h3>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr className="border-b border-gray-200 dark:border-gray-700">
                <th className="text-left py-3 px-4 text-gray-600 dark:text-gray-400">Keyword</th>
                <th className="text-left py-3 px-4 text-gray-600 dark:text-gray-400">Position</th>
                <th className="text-left py-3 px-4 text-gray-600 dark:text-gray-400">Volume</th>
                <th className="text-left py-3 px-4 text-gray-600 dark:text-gray-400">Difficulty</th>
              </tr>
            </thead>
            <tbody>
              {keywordData.map((keyword, index) => (
                <tr key={index} className="border-b border-gray-100 dark:border-gray-700">
                  <td className="py-3 px-4 text-gray-900 dark:text-white font-medium">{keyword.keyword}</td>
                  <td className="py-3 px-4">
                    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
                      keyword.position <= 3 ? 'bg-green-100 text-green-800' :
                      keyword.position <= 10 ? 'bg-yellow-100 text-yellow-800' :
                      'bg-red-100 text-red-800'
                    }`}>
                      #{keyword.position}
                    </span>
                  </td>
                  <td className="py-3 px-4 text-gray-700 dark:text-gray-300">{keyword.volume.toLocaleString()}</td>
                  <td className="py-3 px-4">
                    <div className="flex items-center space-x-2">
                      <div className="w-24 bg-gray-200 dark:bg-gray-700 rounded-full h-2">
                        <div 
                          className={`h-2 rounded-full ${
                            keyword.difficulty > 70 ? 'bg-red-500' :
                            keyword.difficulty > 40 ? 'bg-yellow-500' :
                            'bg-green-500'
                          }`}
                          style={{ width: `${keyword.difficulty}%` }}
                        />
                      </div>
                      <span className="text-xs text-gray-600 dark:text-gray-400">{keyword.difficulty}</span>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}